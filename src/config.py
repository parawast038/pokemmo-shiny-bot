from dataclasses import dataclass
from pathlib import Path
import os
from dotenv import load_dotenv

from src import TEMPLATE_PATH, HISTORY_PATH, LOG_PATH

load_dotenv()


@dataclass
class AppConfig:
    capture_region: tuple[int, int, int, int] = (
        int(os.getenv("CAPTURE_X", "150")),
        int(os.getenv("CAPTURE_Y", "120")),
        int(os.getenv("CAPTURE_WIDTH", "1200")),
        int(os.getenv("CAPTURE_HEIGHT", "800")),
    )
    poll_interval: float = float(os.getenv("POLL_INTERVAL", "0.5"))
    detection_threshold: float = float(os.getenv("DETECTION_THRESHOLD", "0.80"))
    match_method: str = os.getenv("MATCH_METHOD", "cv2")
    discord_webhook: str = os.getenv("DISCORD_WEBHOOK", "")
    game_title: str = os.getenv("GAME_TITLE", "PokéMMO")
    template_path: Path = Path(os.getenv("TEMPLATE_PATH", str(TEMPLATE_PATH)))
    history_path: Path = Path(os.getenv("HISTORY_PATH", str(HISTORY_PATH)))
    log_path: Path = Path(os.getenv("LOG_PATH", str(LOG_PATH)))


APP_CONFIG = AppConfig()
