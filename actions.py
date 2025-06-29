# actions.py

import requests
from config import OPENWEATHER_API_KEY

def get_weather(city_name):
    api_key = OPENWEATHER_API_KEY
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data["cod"] != 200:
            return f"Sorry, I couldn't find weather info for '{city_name}'."

        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]

        return f"The weather in {city_name} is {weather} with a temperature of {temp}°C (feels like {feels_like}°C)."

    except Exception as e:
        return "Sorry, there was a problem fetching the weather."
# actions.py


import re
from database import insert_reminder

def set_reminder(user_id, entities):
    user_input = entities.get("raw_input", "").lower()

    # Extract task using regex: anything after "remind me to" up to "on DATE" or "at TIME"
    task = "your task"
    match = re.search(r"remind me to (.+?)( on | at |$)", user_input)
    if match:
        task = match.group(1).strip()

    date = entities["DATE"] or "unspecified date"
    time = entities["TIME"] or "unspecified time"

    insert_reminder(user_id, task, date, time)
    return f"Reminder set: {task} on {date} at {time} ✅"


def basic_qa(user_input):
    q = user_input.lower()

    if "what is ai" in q:
        return "AI stands for Artificial Intelligence. It refers to machines that can mimic human intelligence."
    elif "who created you" in q or "who made you" in q:
        return "I was created by Gopika as part of an AI assistant project."
    elif "what can you do" in q or "your skills" in q:
        return "I can tell time, check the weather, set reminders, and chat with you!"
    elif "joke" in q:
        return "Why did the computer go to art school? Because it had too many bytes and needed more color!"
    else:
        return "I'm still learning! Please ask me another question."


from database import get_reminders

def show_reminders(user_id):
    reminders = get_reminders(user_id)
    if not reminders:
        return "You have no saved reminders."

    response = "Here are your reminders:\n"
    for task, date, time in reminders:
        response += f"• {task} on {date} at {time}\n"
    return response.strip()

from database import clear_reminders

def delete_all_reminders(user_id):
    clear_reminders(user_id)
    return "All your reminders have been cleared 🗑️"

from database import delete_reminder_by_task

def delete_one_reminder(user_id, user_input):
    # Extract task keyword (simple version)
    if "for" in user_input:
        task_keyword = user_input.split("for", 1)[1].strip()
    else:
        task_keyword = user_input.strip()

    deleted_count = delete_reminder_by_task(user_id, task_keyword)

    if deleted_count > 0:
        return f"Deleted reminder related to '{task_keyword}' 🗑️"
    else:
        return f"No reminder found for '{task_keyword}'."
