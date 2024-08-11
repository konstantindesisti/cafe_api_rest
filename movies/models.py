from . import db
from datetime import datetime
from sqlalchemy import Date, Text, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, unique=True)
    title: Mapped[str] = mapped_column(nullable=False, unique=True)
    year: Mapped[int] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[float] = mapped_column(nullable=False)
    ranking: Mapped[int] = mapped_column(nullable=False)
    review: Mapped[str] = mapped_column()
    img_url: Mapped[str] = mapped_column()

    def __repr__(self) -> str:
        return (f'Movie(id:={self.id}, Movie(title:={self.title},Movie(year:={self.year},'
                f'Movie(description:={self.description},Movie(rating:={self.rating},Movie(ranking:={self.ranking},'
                f'Movie(review:={self.review},Movie(img_url:={self.img_url}')
