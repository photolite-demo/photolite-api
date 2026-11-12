from fastapi import FastAPI

app = FastAPI(title="Photo Lite API")


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}
