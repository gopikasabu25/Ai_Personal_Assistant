from flask import Flask, request, jsonify
from nlp_engine import intent_recognizer, extract_entities
from utils import get_user_name, set_user_name
from actions import get_weather, set_reminder, basic_qa
from actions import show_reminders,delete_all_reminders,delete_one_reminder
from flask import Flask, request, jsonify, render_template
from database import get_reminders


app = Flask(__name__)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/", methods=["GET"])
def home():
    return render_template("chat.html")


@app.route("/chat-ui")
def chat_ui():
    return render_template("chat.html")

@app.route("/calendar")
def calendar_ui():
    return render_template("calendar.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_input = data.get("message", "")
    user_id = data.get("user_id", "default")
    

    # Step 1: Recognize intent
    intent = intent_recognizer(user_input)

    # Step 2: Extract entities using spaCy
    entities = extract_entities(user_input)
    entities["raw_input"] = user_input
    intent = intent_recognizer(user_input)

    print(f"Intent: {intent} | Entities: {entities}")


    # Step 3: Personalization handling
    if intent == "set_user_name" and entities["PERSON"]:
        set_user_name(user_id, entities["PERSON"])
        return jsonify({"response": f"Nice to meet you, {entities['PERSON']}!"})

    # Step 4: Handle other intents
    if intent == "greet":
        name = get_user_name(user_id)
        if name:
            return jsonify({"response": f"Hello {name}, how can I help you today?"})
        else:
            return jsonify({"response": "Hello! What's your name?"})

    elif intent == "time_now":
        from datetime import datetime
        now = datetime.now().strftime("%I:%M %p")
        return jsonify({"response": f"The current time is {now}."})
    
    elif intent == "get_weather":
        city = entities["GPE"] or "your city"
        weather_report = get_weather(city)
        return jsonify({"response": weather_report})
    
    elif intent == "set_reminder":
        reminder_response = set_reminder(user_id, entities)
        return jsonify({"response": reminder_response})
    
    elif intent == "delete_one_reminder":
        return jsonify({"response": delete_one_reminder(user_id, user_input)})

    elif intent == "clear_reminders":
       return jsonify({"response": delete_all_reminders(user_id)})

    elif intent == "show_reminders":
        return jsonify({"response": show_reminders(user_id)})
    
    elif intent == "basic_qa":
        answer = basic_qa(user_input)
        return jsonify({"response": answer})


    elif intent == "fallback":
        return jsonify({"response": "I'm not sure how to respond to that. Can you rephrase?"})

    # Placeholder for other features
    return jsonify({
        "response": f"Intent recognized: {intent}",
        "entities": entities
    })

from datetime import datetime, timedelta

def convert_date_to_iso(date_str):
    # Handles weekday names like "Friday"
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    date_str = date_str.strip().lower()

    if date_str in weekdays:
        today = datetime.today()
        current_weekday = today.weekday()
        target_weekday = weekdays.index(date_str)

        days_ahead = (target_weekday - current_weekday) % 7
        if days_ahead == 0:
            days_ahead = 7  # move to next week if same day
        target_date = today + timedelta(days=days_ahead)
        return target_date.strftime("%Y-%m-%d")

    try:
        # Try parsing as full date, e.g., "July 1", "August 10"
        parsed = datetime.strptime(date_str, "%B %d")
        this_year = datetime.today().year
        return f"{this_year}-{parsed.month:02d}-{parsed.day:02d}"
    except:
        return None
def convert_time_to_24h(time_str):
    try:
        return datetime.strptime(time_str.strip(), "%I:%M %p").strftime("%H:%M:%S")
    except:
        return "00:00:00"

from database import get_reminders

@app.route("/reminders-json", methods=["GET"])
def reminders_json():
    user_id = "default"
    reminders = get_reminders(user_id)

    events = []
    for task, date, time in reminders:
        if date != "unspecified date" and time != "unspecified time":
            try:
                # Convert date and time to valid ISO format
                date_iso = convert_date_to_iso(date)
                time_iso = convert_time_to_24h(time)
                events.append({
                    "title": task,
                    "start": f"{date_iso}T{time_iso}"
                })
            except:
                continue
    return jsonify(events)


# ✅ Flask app must run after all routes are defined
if __name__ == "__main__":
    import os
    import webbrowser

    # Only run on first launch (not on Flask reload)
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        webbrowser.open("http://127.0.0.1:5000/dashboard")

    app.run(debug=True)

