from fastapi import APIRouter, HTTPException
from services.random_word_service import RandomWordService

router = APIRouter(prefix="/api/random-word", tags=["Random Word"])
service = RandomWordService()


@router.get("/get_random_word")
async def get_random_word():
    """
    Devuelve una palabra aleatoria de una lista predefinida
    """
    try:
        random_word = service.get_random_word()
        return {
            "success": True,
            "word": random_word
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
