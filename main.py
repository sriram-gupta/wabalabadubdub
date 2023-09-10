from fastapi import FastAPI
app = FastAPI()

@app.get("/health")
def HealthCheck():
    return { "status": "ok", "msg": "Health Check Working Properly" }

