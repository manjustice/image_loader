__all__ = ["Image"]

from sqlalchemy.orm import relationship

from app.core.database import Base
from sqlalchemy import Column, String, Integer, ForeignKey


class Image(Base):
    __tablename__ = "user_images"

    id = Column(Integer, primary_key=True)
    url = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("telegram_users.id"))

    user = relationship("TelegramUser", back_populates="images")
