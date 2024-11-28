from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-goes-here')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

# 路由
@app.route('/')
def home():
    return render_template('index.html', title='Portfolio')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/game')
def game():
    return render_template('game.html', title='Play Game')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/send-message', methods=['POST'])
def send_message():
    try:
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # 创建邮件
        msg = MIMEMultipart()
        msg['From'] = os.getenv('EMAIL_USER')
        msg['To'] = os.getenv('EMAIL_USER')  # 发送给自己
        msg['Subject'] = f"Portfolio Contact: Message from {name}"

        body = f"""
        Name: {name}
        Email: {email}
        Message:
        {message}
        """
        msg.attach(MIMEText(body, 'plain'))

        # 发送邮件
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASSWORD'))
        text = msg.as_string()
        server.send_message(msg)
        server.quit()

        flash('Message sent successfully!', 'success')
    except Exception as e:
        app.logger.error(f"Error sending email: {e}")
        flash('Sorry, there was an error sending your message. Please try again later.', 'error')

    return redirect(url_for('contact'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=3000)
