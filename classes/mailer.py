import os
from flask import current_app
import sendgrid
from sendgrid.helpers.mail import *

class Mailer:

    def __init__(self, request_id: str, payload: dict):
        self.request_id = request_id
        self.payload = payload

    def send(self):
        message = Mail(
        from_email=self.payload['from_email'],
        to_emails=self.payload['to_email'],
        subject=self.payload['subject'],
        html_content=self.payload['html_content'])
        try:
            sg = sendgrid.SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            current_app.logger.info(response.status_code)
            current_app.logger.info(response.body)
            current_app.logger.info(response.headers)
            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- Email sent successfully")
            return {"status": "SUCCESS", "message": "Email sent successfully", "response": response}
        except Exception as e:
            current_app.logger.error(f"{self.request_id} --- {self.__class__.__name__} --- {str(e)}")
            return {"status": "FAILED", "message": "Email failed to send", "error": str(e)}