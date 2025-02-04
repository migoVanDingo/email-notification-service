import traceback
from flask import current_app
from api.email.payload.payload_send_account_verification import PayloadSendAccountVerification
from classes.mailer import Mailer
from interface.abstract_handler import AbstractHandler
from utility.constant import Constant
from utility.request import Request


class RequestSendAccountVerification(AbstractHandler):
    def __init__(self, request_id: str, payload: dict):
        self.request_id = request_id
        self.payload = payload

    def do_process(self):
        try:
            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- SEND_ACCOUNT_VERIFICATION_EMAIL")

            # Get user email
            dao_request = Request()
            user_response = dao_request.query(self.request_id, f"SELECT email, username FROM user WHERE user_id = '{self.payload['user_id']}'")

            current_app.logger.info(f"{self.request_id} --- {self.__class__.__name__} --- USER RESPONSE: {user_response}")

            user = user_response['response']

            user_email = user[0]['email']

            # Form email verification URL
            url = f"{Constant.base_url}{Constant.frontend_port}{Constant.email['ACCOUNT_VERIFICATION']['ENDPOINT']}?token={self.payload['token']}"

            mailer = Mailer(self.request_id, PayloadSendAccountVerification.form_account_verification_payload(Constant.email['ACCOUNT_VERIFICATION']['FROM_EMAIL'], user_email, Constant.email['ACCOUNT_VERIFICATION']['SUBJECT'], self.generate_verification_email_content(url)))

            response = mailer.send()

            return response
        except Exception as e:
            current_app.logger.error(f"{self.request_id} --- {self.__class__.__name__} --- {traceback.format_exc()} --- {str(e)}")
            return {"status": "FAILED", "error": str(e)}
        

    def generate_verification_email_content(self, url: str) -> str:
        html_content = f"""
        <html>
        <body>
            <p>Dear user,</p>
            <p>Thank you for registering with CloudNeuros!</p>
            <p>Please click the link below to verify your account:</p>
            <p>
                <a href="{url}" target="_blank">Verify your CloudNeuros account</a>
            </p>
            <p>If you did not request this, please ignore this email.</p>
            <p>Best regards,<br>CloudNeuros Team</p>
        </body>
        </html>
        """
        return html_content