import os
import traceback
from flask import Flask
from werkzeug.exceptions import InternalServerError
import sendgrid
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
sg = sendgrid.SendGridAPIClient()

def create_message(email_text):
    return sendgrid.helpers.mail.Mail(
        from_email=os.environ["FROM_EMAIL"],
        to_emails=os.environ["TO_EMAIL"],
        subject='[my app] unhandled exception occurred!',
        plain_text_content=email_text,
    )

@app.errorhandler(InternalServerError)
def handle_500(e):
    error_tb = traceback.format_exc()
    try:
        resp = sg.send(create_message(error_tb))
    except Exception as exc:
        print(exc.message)
    return app.finalize_request(e, from_error_handler=True) 

class BigBangException(Exception):
    pass

@app.route("/")
def index():
    raise BigBangException("Something bad happened here..")
    return "Helloworld!"
