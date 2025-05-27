print("Importing modules...")

from flask import Flask, request, jsonify, send_from_directory
import smtplib
from email.message import EmailMessage
from waitress import serve

print("Modules imported.")

app = Flask(__name__)

# Add one here too:
print("App created.")


# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'auseremailsender@gmail.com'       # Replace with your email
SENDER_PASSWORD = 'uguj tclg kcrx qkvv'           # Use an app-specific password
RECEIVER_EMAIL = 'auseremailsender@gmail.com'

@app.route('/')
def serve_form():
    return send_from_directory('.', 'index.html')

@app.route('/sendmail', methods=['POST'])
def send_mail():
    try:
        name = request.form.get('name', '')
        phone = request.form.get('phone', '')
        email = request.form.get('email', '')
        service = request.form.get('service', '')
        dog_info = request.form.get('dogInfo', '')

        message = EmailMessage()
        message['Subject'] = 'Nuova Prenotazione Consulenza'
        message['From'] = SENDER_EMAIL
        message['To'] = RECEIVER_EMAIL

        body = f"""
Hai ricevuto una nuova richiesta di consulenza:

Nome: {name}
Telefono: {phone}
Email: {email}
Servizio: {service}

Informazioni sul cane:
{dog_info}
"""
        message.set_content(body)

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(message)

        return "success"

    except Exception as e:
        print("Error:", e)
        return "error", 500

if __name__ == '__main__':
    print("Starting Waitress on http://0.0.0.0:8080")
    serve(app, host='0.0.0.0', port=5000)
