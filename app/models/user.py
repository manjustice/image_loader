__all__ = ["TelegramUser"]

from sqlalchemy.orm import relationship

from app.core.database import Base
from sqlalchemy import Column, String, Integer


class TelegramUser(Base):
    __tablename__ = "telegram_users"

    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)

    images = relationship("Image", back_populates="user")
