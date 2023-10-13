import os
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import  load_dotenv
import requests

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
@app.route('/')
def index():
    return render_template('index.html')

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    social = db.Column(db.String(50), nullable=False)
    nationality = db.Column(db.String(50), nullable=False)
    family = db.Column(db.String(50), nullable=False)
    animal = db.Column(db.String(50), nullable=False)
    date_move_in = db.Column(db.String(50), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    rooms_number = db.Column(db.String(50), nullable=False)
    budget = db.Column(db.String(50), nullable=False)
    meters = db.Column(db.String(50), nullable=False)
    parking = db.Column(db.String(50), nullable=False)
    work_info = db.Column(db.String(50), nullable=False)
    wishes = db.Column(db.String(50), nullable=False)

@app.route('/form-submitted', methods=['POST'])

def submit_form():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    social = request.form['social_media']
    nationality = request.form['citizenship']
    family = request.form['family']
    animal = request.form['animals']
    date_move_in = request.form['settlement_date']
    city = request.form['city']
    rooms_number = request.form['roomsAmount']
    budget = request.form['price']
    meters = request.form['apartment_area']
    parking = request.form['Parking']
    work_info = request.form['work_info']
    wishes = request.form['heardAboutUs']

    new_user = User(
        name=name, email=email, phone=phone, social=social, 
        nationality=nationality, family=family, animal=animal, 
        date_move_in=date_move_in, city=city, rooms_number=rooms_number, 
        budget=budget, meters=meters, parking=parking, 
        work_info=work_info, wishes=wishes
    )
    db.session.add(new_user)
    db.session.commit()

    # Send to Telegram
    telegram_bot_token = os.getenv('telegram_bot_token')
    chat_id = os.getenv('chat_id')
    text = (
        f"New user\n"
        f"Name: {name}\n"
        f"Email: {email}\n"
        f"Phone: {phone}\n"
        f"Social networks: {social}\n"
        f"Nationality: {nationality}\n"
        f"Family: {family}\n"
        f"Animal: {animal}\n"
        f"Date move in: {date_move_in}\n"
        f"City: {city}\n"
        f"appartment: {rooms_number}\n"
        f"Budget: {budget}\n"
        f"Meters: {meters}\n"
        f"Parking: {parking}\n"
        f"Work info: {work_info}\n"
        f"Wishes: {wishes}\n"
    )
    send_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={chat_id}&text={text}"
    requests.get(send_url)

    return render_template('formSubmitted.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5050)
