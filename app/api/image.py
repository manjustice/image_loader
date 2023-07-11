from fastapi import APIRouter
from fastapi.responses import FileResponse

image_router = APIRouter(prefix="/images")


@image_router.get("/{filename}")
async def get_image(filename: str):
    image_path = f"images/{filename}"
    return FileResponse(image_path)
