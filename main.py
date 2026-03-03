import settings
import uvicorn
from fastapi import FastAPI

app = FastAPI(
    servers=[
        {"url": "https://dev-be-ai.20206205.tech", "description": "Dev Server"},
        {"url": "https://be-ai.20206205.tech", "description": "Prod Server"},
    ],
)


@app.get("/")
def root():
    return {
        "message": "Hello World",
        "docs": "/docs"
    }


def main():
    uvicorn.run("main:app", host=settings.IP, port=settings.PORT, reload=True)


if __name__ == "__main__":
    main()
