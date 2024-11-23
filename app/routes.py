from flask import render_template, request, redirect, url_for, jsonify
from app import app, db
from app.models import User, ParkingSlot
from app.lpr import recognize_plate
from app.parking_allocation import allocate_slot

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/monitor')
def monitor():
    slots = ParkingSlot.query.all()
    return render_template('monitor.html', slots=slots)

@app.route('/allocate', methods=['POST'])
def allocate():
    license_plate = request.form.get('license_plate')
    recognized_plate = recognize_plate(license_plate)
    slot = allocate_slot(recognized_plate)
    if slot:
        return jsonify({"success": True, "slot": slot.slot_number})
    return jsonify({"success": False, "message": "No slots available"})
