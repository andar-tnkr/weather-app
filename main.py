import tkinter as tk
from tkinter import messagebox
import requests
import os  # Standard library for operating system interactions
from dotenv import load_dotenv # Import the helper we just installed

# 1. Load the variables from the .env file
load_dotenv()

# 2. Get the key securely
API_KEY = os.getenv("API_KEY")

# Check if the key loaded correctly (Optional safety check)
if not API_KEY:
    messagebox.showerror("Error", "API Key not found! Make sure .env file exists.")

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name!")
        return

    # Construct the API request URL
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}&units=metric"
    
    try:
        # Send the request to the server
        response = requests.get(request_url)
        data = response.json()
        
        # Check if the city was found (HTTP 200 means OK)
        if response.status_code == 200:
            # Parse the JSON data
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']
            wind_speed = data['wind']['speed']
            
            # Update the GUI labels
            temp_label.config(text=f"{temp}°C")
            desc_label.config(text=f"{description.title()}")
            details_label.config(text=f"Humidity: {humidity}% | Wind: {wind_speed} m/s")
        else:
            # If city not found or other API error
            messagebox.showerror("Error", f"City not found or API error.\nCode: {response.status_code}")
            
    except Exception as e:
        messagebox.showerror("Connection Error", f"Could not connect to service.\nError: {e}")

# --- GUI SETUP ---
root = tk.Tk()
root.title("Python Weather App")
root.geometry("350x400")
root.configure(bg="#f0f0f0") # Light gray background

# 1. Title
title_label = tk.Label(root, text="Weather Search", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=20)

# 2. Input Field
city_entry = tk.Entry(root, font=("Helvetica", 14), width=20, justify='center')
city_entry.pack(pady=5)
city_entry.focus() # Places cursor in box automatically

# 3. Search Button
search_btn = tk.Button(root, text="Get Weather", font=("Helvetica", 12), bg="#007bff", fg="white", command=get_weather)
search_btn.pack(pady=10)

# 4. Weather Output Area
# Frame to hold weather info nicely
weather_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
weather_frame.pack(pady=20, padx=20, fill="both", expand=True)

temp_label = tk.Label(weather_frame, text="--°C", font=("Helvetica", 30, "bold"), bg="white", fg="#ff5722")
temp_label.pack(pady=(20, 5))

desc_label = tk.Label(weather_frame, text="---", font=("Helvetica", 14, "italic"), bg="white")
desc_label.pack(pady=5)

details_label = tk.Label(weather_frame, text="Humidity: -- | Wind: --", font=("Helvetica", 10), bg="white")
details_label.pack(pady=10)

# Run the App
root.mainloop()