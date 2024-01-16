from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.backend.session import create_session
from app.schemas.movies import MovieSchema
from app.services.movies import MovieService

router = APIRouter(prefix="/movies")


@router.get("/", response_model=MovieSchema)
async def get_movie(
        movie_id: int, session: Session = Depends(create_session)
) -> MovieSchema:
    return MovieService(session).get_movie(movie_id)


@router.get("/new", response_model=List[MovieSchema])
async def get_new_movies(
        year: int, rating: float, session: Session = Depends(create_session)
) -> List[MovieSchema]:
    return MovieService(session).get_new_movies(year, rating)
