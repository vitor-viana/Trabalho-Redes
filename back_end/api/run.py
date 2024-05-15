from fastapi import FastAPI
import uvicorn
from controller.email_controller import router

app = FastAPI()

if __name__ == "__main__":
    app.include_router(router, prefix="/api/email")
    uvicorn.run(app, host="0.0.0.0", port=8000)
