# Smart Parking System in Universities

## Description
A sensor-less smart parking management system leveraging deep learning and License Plate Recognition (LPR) to optimize parking allocation. 

## Features
- Automatic License Plate Recognition
- Real-Time Parking Slot Monitoring
- Priority Parking Allocation

## Tools & Technology
- Python, Flask
- SQLite for database management
- OpenCV for LPR
- Google Maps API (Optional)

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Initialize the database:
4. Run the application:
5. Access the application at `http://localhost:5000`.

## License
MIT License

## How to Run:
Database Initialization: Run the following commands in Python:

from app import db
db.create_all()

Run the App: Start the Flask application:

python manage.py runserver
Access the App: Open http://127.0.0.1:5000 in your browser.