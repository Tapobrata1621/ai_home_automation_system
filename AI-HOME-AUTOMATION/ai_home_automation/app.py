from flask import Flask, render_template, request, jsonify
try:
    from devices import toggle_device, get_device_states
except ImportError:
    raise ImportError("The 'devices' module could not be found. Ensure 'devices.py' exists in the same directory as 'app.py'.")
from ai_engine import ai_interpret_command

app = Flask(__name__)

# ---------------- HOME ROUTE ----------------
@app.route("/")
def home():
    return render_template("index.html", devices=get_device_states())


# ---------------- AI COMMAND ROUTE ----------------
@app.route("/command", methods=["POST"])
def command():
    data = request.get_json()
    user_command = data.get("command", "")
    device, state = ai_interpret_command(user_command)

    if device is None:
        return jsonify({"success": False, "message": "Command not recognized by AI."})

    toggle_device(device, state)

    return jsonify({
        "success": True,
        "message": f"{device.capitalize()} {'turned on' if state else 'turned off'}",
        "devices": get_device_states()
    })


# ---------------- ROOMS PAGE ----------------
@app.route("/rooms")
def rooms_page():
    rooms = [
        {"name": "Living Room", "devices": ["Light", "AC", "TV"], "icon": "🛋️"},
        {"name": "Bedroom", "devices": ["Fan", "Lamp", "TV"], "icon": "🛏️"},
        {"name": "Kitchen", "devices": ["Light", "Fridge", "Microwave"], "icon": "🍳"},
        {"name": "Bathroom", "devices": ["Light", "Heater"], "icon": "🚿"},
        {"name": "Dining Room", "devices": ["Light", "Fan"], "icon": "🍽️"},
        {"name": "Kids Room", "devices": ["Lamp", "Fan", "Toy Light"], "icon": "🧸"},
        {"name": "Office", "devices": ["PC", "Light", "AC"], "icon": "💻"},
    ]
    return render_template("rooms.html", rooms=rooms)


# ---------------- DEVICES PAGE ----------------
@app.route("/devices")
def devices_page():
    devices = [
        {"name": "Light", "room": "Living Room", "status": "ON", "last_active": "2 hrs ago"},
        {"name": "AC", "room": "Bedroom", "status": "OFF", "last_active": "1 hr ago"},
        {"name": "Fan", "room": "Kids Room", "status": "ON", "last_active": "30 mins ago"},
        {"name": "Refrigerator", "room": "Kitchen", "status": "ON", "last_active": "Always"},
        {"name": "Lamp", "room": "Bedroom", "status": "OFF", "last_active": "5 hrs ago"},
    ]
    return render_template("devices.html", devices=devices)


# ---------------- ENERGY PAGE ----------------
@app.route("/energy")
def energy_page():
    current_temp = 24
    humidity = 58
    usage = [3.4, 2.8, 3.6, 2.9, 3.2, 3.8, 4.0]  # 7 days chart data

    return render_template(
        "energy.html",
        temp=current_temp,
        humidity=humidity,
        usage=usage
    )



# ---------------- SETTINGS PAGE ----------------
@app.route("/settings")
def settings_page():
    return render_template("settings.html")


# ---------------- RUN APPLICATION ----------------
if __name__ == "__main__":
    app.run(debug=True)
