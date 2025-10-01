from fastapi import APIRouter
from fastapi.responses import JSONResponse
import random
import logging

logger = logging.getLogger("app")

router = APIRouter(prefix="/random-word", tags=["Random Word"])

RANDOM_WORDS = [
    "banana", "elephant", "guitar", "rainbow", "mountain",
    "chocolate", "butterfly", "ocean", "adventure", "starlight",
    "whisper", "journey", "firefly", "sunrise", "melody",
    "cosmic", "dragon", "crystal", "thunder", "magic"
]

@router.get("/get_random_word")
async def get_random_word():
    """
    Devuelve una palabra aleatoria de una lista predefinida
    """
    logger.info("🎲 /random-word - Obteniendo palabra aleatoria")

    try:
        random_word = random.choice(RANDOM_WORDS)

        logger.info(f"✅ Palabra seleccionada: {random_word}")

        return JSONResponse(content={
            "success": True,
            "word": random_word
        })

    except Exception as e:
        logger.error(f"❌ Error obteniendo palabra aleatoria: {e}")
        return JSONResponse(content={
            "success": False,
            "error": str(e),
            "word": "error"
        }, status_code=500)
