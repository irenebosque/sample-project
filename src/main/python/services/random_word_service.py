import random
import logging

logger = logging.getLogger("app")


class RandomWordService:
    """Service for random word generation"""

    RANDOM_WORDS = [
        "banana", "elephant", "guitar", "rainbow", "mountain",
        "chocolate", "butterfly", "ocean", "adventure", "starlight",
        "whisper", "journey", "firefly", "sunrise", "melody",
        "cosmic", "dragon", "crystal", "thunder", "magic"
    ]

    def get_random_word(self) -> str:
        """Get a random word from the list"""
        logger.info("🎲 Getting random word")
        random_word = random.choice(self.RANDOM_WORDS)
        logger.info(f"✅ Selected word: {random_word}")
        return random_word
