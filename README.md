# 🤖 AI Personal Assistant with Calendar Integration

This project is a smart AI-powered personal assistant that helps users manage tasks through natural language conversations. Built with Python (Flask), NLP (spaCy). it combines real-time chat with a visual calendar interface.

---

## ✨ Features

- 💬 **Conversational Chatbot UI**
  - Recognizes intents like greetings, scheduling, weather, and basic Q&A
  - Personalized interaction (remembers user name)

- 📝 **Task Scheduling**
  - Users can type: `"Remind me to attend class on Friday at 10 AM"`
  - Reminder is stored with date and time using NLP

- 📅 **Interactive Calendar**
  - Visual calendar 
  - Automatically displays scheduled reminders
  - Calendar updates live after each task

- ⏰ **Current Time & Date Query**
  - Responds to "What is the time now?" with live time

- 🌤️ **Weather Integration**
  - Gets real-time weather data using OpenWeatherMap API

- ❌ **Reminder Deletion**
  - Delete a specific reminder: `"Delete reminder for AI workshop"`
  - Clear all: `"Clear all reminders"`

- 🧠 **Rule-Based Q&A**
  - Responds to basic questions like "Tell me a joke" or "What is AI?"

---

## 🔧 Tech Stack

| Layer        | Tools                        |
|--------------|------------------------------|
| Backend      | Flask (Python)               |
| Frontend     | HTML + JavaScript            |
| NLP Engine   | spaCy                        |
| Calendar     | FullCalendar.js              |
| Database     | SQLite                       |
| API          | OpenWeatherMap               |

---
## 🚀 How to Run

1. 🔃 Clone this repository


2. 🛠️ Install dependencies


pip install flask spacy requests
python -m spacy download en_core_web_sm

3. 🔐 Weather API Configuration

This project uses the OpenWeatherMap API to fetch real-time weather updates based on user queries like:

##### “What’s the weather in Kochi?”

To use this feature, you need to provide your own API key securely via a config.js file.

### ⚙️ Setup Instructions

Follow these steps to set up your weather API:

1. Get an API Key

Visit https://openweathermap.org/api

Sign up and generate a free API key

2. Create config.js

In the root directory of your project (same level as app.py), create a new file named as config.js

3. Paste the Following Code:

// config.js
const OPENWEATHER_API_KEY = "your_openweathermap_api_key_here";

🔁 Replace "your_openweathermap_api_key_here" with your actual key.


4. ▶️ Run the app

python app.py

5. 🌐 Open in browser

http://127.0.0.1:5000/dashboard

[!Screenshot](https://github.com/gopikasabu25/Ai_Personal_Assistant/blob/main/Assistant.png)

[!Screenshot](https://github.com/gopikasabu25/Ai_Personal_Assistant/blob/main/Assistant2.png)

##  Sample Try

| User Input                                      | Bot Response                                 |
| ----------------------------------------------- | -------------------------------------------- |
| hi                                              | Hello! What's your name?                     |
| I am Gopika                                     | Nice to meet you, Gopika!                    |
| Remind me to attend AI seminar on Friday at 2PM | Reminder set: attend AI seminar... ✅        |
| What's the weather in Kochi?                    | The weather in Kochi is...                   |
| What are my reminders?                          | Lists all saved reminders                    |
| Delete reminder for AI seminar                  | Deleted reminder related to 'AI seminar' 🗑️ |
| Clear all reminders                             | All your reminders have been cleared 🗑️     |


## ⚖️ API License
This project uses the free tier of the OpenWeatherMap API, which is licensed for public non-commercial use under the OpenWeather Terms of Service.

Please ensure you have a valid API key from https://openweathermap.org/appid and follow their usage guidelines.
