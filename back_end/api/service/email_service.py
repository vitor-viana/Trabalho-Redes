import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config.email_config import EmailConfig
from fastapi import HTTPException

class EmailService:
    def __init__(self):
        self.smtp_server = EmailConfig.SMTP_SERVER
        self.smtp_port = EmailConfig.SMTP_PORT
        self.smtp_username = EmailConfig.SMTP_USERNAME
        self.smtp_password = EmailConfig.SMTP_PASSWORD

    def send_email(self, to_email:str, subject:str, body:str):
        msg = MIMEMultipart()
        msg['From'] = self.smtp_username
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.send_message(msg)
            return True
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Erro ao enviar e-mail: {str(e)}")

email_service = EmailService()
