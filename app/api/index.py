from fastapi import Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter


from app.utils.get_session import get_session
from app.utils.get_users import get_users

index_router = APIRouter()

templates = Jinja2Templates(directory="templates")


@index_router.get("/")
async def index(
        request: Request,
        db_session: AsyncSession = Depends(get_session)
):
    users = await get_users(db_session)

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "users": users}
    )
