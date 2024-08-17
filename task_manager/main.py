from fastapi import FastAPI

from task_manager.settings import settings

app = FastAPI()


@app.get(settings.status_url)
async def status():
    return {"status": "ok"}
