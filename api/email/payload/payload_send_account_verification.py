class PayloadSendAccountVerification:

    @staticmethod
    def form_account_verification_payload(from_email, to_email, subject, html_content) -> dict:
        payload = {
            "from_email": from_email,
            "to_email": to_email,
            "subject": subject,
            "html_content": html_content
        }
        return payload