from fastapi import FastAPI

app = FastAPI()

# Default root endpoint
@app.get("/")
async def root():
  return { "message": "To add to the API go to the Github! " }
