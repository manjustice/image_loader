from fastapi import FastAPI

from app.api.index import index_router
from app.api.image import image_router

app = FastAPI()

app.include_router(index_router)
app.include_router(image_router)


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
