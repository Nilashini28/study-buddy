from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API working"}

@app.get("/favicon.png")
def favicon():
    return JSONResponse(content={}, status_code=204)