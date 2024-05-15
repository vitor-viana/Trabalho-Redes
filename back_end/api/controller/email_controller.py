from fastapi import APIRouter, Form
from service.email_service import email_service

router = APIRouter()

@router.post("/send/")
async def send_email(to_email:str = Form(...), subject:str = Form(...), body:str = Form(...)):
    success = email_service.send_email(to_email, subject, body)
    if success:
        return {"message": "E-mail enviado com sucesso!"}
  