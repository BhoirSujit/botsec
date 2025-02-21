import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from config import SERVER_HOST, SERVER_PORT

app = FastAPI()

# Request Model
class LinkRequest(BaseModel):
    link: str

@app.get("/")
async def root():
    return {"message": "🤖 Telegram Bot API is running!"}

@app.post("/verifylink")
async def verifylink(data: LinkRequest):
    print("🆕 New Request:", data)

    # List of known malicious links (replace with actual detection logic)
    malicious_links = ["https://google.com"]

    # Check if the link is malicious
    is_malicious = data.link in malicious_links

    return {
        "link": data.link,
        "is_malicious": is_malicious
    }

if __name__ == "__main__":
    uvicorn.run(app, host=SERVER_HOST, port=SERVER_PORT)
