import os
from flask import Flask, request, send_file
import csv
import pyttsx3

app = Flask(__name__)
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def save_details(name, email, filename="users.csv"):
    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, email])

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()

        if name and email:
            save_details(name, email)
            speak(f"Registration completed successfully, welcome {name}!")
            return "✅ Registration successful!"
        return "⚠️ Please fill all fields!"

    return send_file(os.path.join(os.path.dirname(__file__), "index.htm"))

if __name__ == "__main__":
    app.run(debug=True)
