from flask import Flask, render_template, request
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
        name = request.form["name"]
        email = request.form["email"]

        if name and email:
            save_details(name, email)
            speak(f"Registration completed successfully, welcome {name}!")
            return "✅ Registration successful!"
        else:
            return "⚠️ Please fill all fields!"
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
