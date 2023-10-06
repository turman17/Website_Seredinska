from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    property = db.Column(db.String(50), nullable=False)

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    property = request.form['property']

    # Store in SQLite Database
    new_user = User(name=name, email=email, phone=phone, property=property)
    db.session.add(new_user)
    db.session.commit()

    # Send to Telegram
    telegram_bot_token = "your telegram bot token"
    chat_id = "your chat id"
    text = f"New user\nName: {name}\nGmail: {email}\nPhone: {phone}\nInterested In: {property}"

    send_url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage?chat_id={chat_id}&text={text}"
    requests.get(send_url)

    return 'Form submitted'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
