# 🌤️ Python Weather GUI

A clean and simple desktop weather application built with Python and Tkinter. It fetches real-time weather data (temperature, humidity, wind speed) using the OpenWeatherMap API.

## 📸 Features
- **Real-time Data:** Fetches live weather updates.
- **GUI Interface:** User-friendly window built with Tkinter.
- **Secure:** Uses environment variables to handle API keys safely.
- **Error Handling:** Manages invalid city names and connection errors gracefully.

## 🛠️ Installation & Setup

1. Clone the repository
   git clone [https://github.com/andar-tnkr/weather-app.git](https:https://github.com/andar-tnkr/weather-app)
   cd weather-app

2. Install dependencies

type command "python -m pip install -r requirements.txt"

3. Configure API Key
- Sign up at OpenWeatherMap to get a free API key.
- Rename .env.example to .env.
- Open .env and paste your API key:
    API_KEY=your_actual_api_key_here

4. Run the App

type "python main.py"

Tech Stack :
- Python 3.x
- Tkinter (GUI)
- Requests (HTTP Calls)
- Python-Dotenv (Security)