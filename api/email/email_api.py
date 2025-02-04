from flask import Blueprint, g, json, request
import os
import sendgrid
from sendgrid.helpers.mail import *

from api.email.handler.request_send_account_verification import RequestSendAccountVerification


email_api = Blueprint('email_api', __name__)

@email_api.route('/email/send/verification', methods=['POST'])
def send_verification_email():
    data = json.loads(request.data)
    if "request_id" in data:
        request_id = data['request_id']
    elif "job_id" in data:
        request_id = data['job_id']
    else:
        request_id = g.request_id

    api_request = RequestSendAccountVerification(request_id, data)
    response = api_request.do_process()

    if response['status'] == "SUCCESS":
        data['job_result'] = response["message"]
        del data['token']
        return {"status": "SUCCESS", "data": data}


    return response
    

""" @email_api.route('/send', methods=['GET'])
def send_email():
    # using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python


    message = Mail(
    from_email='admin@cloudneuros.com',
    to_emails='mlujan476@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return "Email sent successfully"
    except Exception as e:
        print(e.message)
        return "Email failed to send" """