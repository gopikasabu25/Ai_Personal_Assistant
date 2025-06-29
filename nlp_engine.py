# nlp_engine.py

import spacy

# Load spaCy model once
nlp = spacy.load("en_core_web_sm")

def intent_recognizer(user_input):
    user_input = user_input.lower()

    if any(x in user_input for x in ["delete all reminders", "clear all reminders", "remove reminders"]):
      return "clear_reminders"
    
    elif "delete reminder for" in user_input or "remove reminder for" in user_input:
         return "delete_one_reminder"


    elif any(x in user_input for x in ["what are my reminders", "show my tasks", "list my reminders", "reminders", "my tasks"]):
        return "show_reminders"

    elif "remind me" in user_input or "set a reminder" in user_input:
        return "set_reminder"

    elif any(phrase in user_input for phrase in ["my name is", "name is", "i am", "i'm", "this is"]):
        return "set_user_name"

    elif "weather" in user_input:
        return "get_weather"

    elif "time" in user_input:
        return "time_now"

    elif "schedule" in user_input or "meeting" in user_input or "event" in user_input:
        return "schedule_task"
    elif any(q in user_input for q in [
        "what is ai", "who created you", "who made you", "what can you do",
        "your skills", "tell me a joke", "say something smart"
    ]):
        return "basic_qa"

    elif any(greet in user_input for greet in ["hello", "hi", "hey"]):
        return "greet"

    return "fallback"


# Named Entity Recognition (NER)
def extract_entities(user_input: str):
    doc = nlp(user_input)
    entities = {
        "PERSON": None,
        "GPE": None,          # City/Location
        "DATE": None,
        "TIME": None
    }
    for ent in doc.ents:
        if ent.label_ in entities:
            entities[ent.label_] = ent.text
    return entities
