from __future__ import annotations

import json
import time
from pathlib import Path
from datetime import datetime

from src.capture import capture_region, save_debug_screenshot
from src.config import APP_CONFIG
from src.detector import ShinyDetector
from src.logger import setup_logger
from src.notifications import notify_shiny


def load_history(history_path: str | Path):
    path = Path(history_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    if not path.exists():
        return {"encounter_count": 0, "shiny_events": []}

    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"encounter_count": 0, "shiny_events": []}


def save_history(history, history_path: str | Path):
    path = Path(history_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)


def main():
    logger = setup_logger(APP_CONFIG.log_path)
    detector = ShinyDetector(APP_CONFIG.template_path, threshold=APP_CONFIG.detection_threshold)
    history = load_history(APP_CONFIG.history_path)

    last_frame = None
    encounter_count = int(history.get("encounter_count", 0))

    logger.info("PokéMMO Shiny Bot iniciado")
    logger.info(f"Región: {APP_CONFIG.capture_region}")

    if not detector.has_template():
        logger.warning(
            "No se encontró la plantilla de shiny en %s. "
            "Colócala ahí para activar la detección visual.",
            APP_CONFIG.template_path,
        )

    while True:
        try:
            frame = capture_region(APP_CONFIG.capture_region)

            if last_frame is not None:
                delta = detector.image_difference(last_frame, frame)
                if delta > 5:
                    encounter_count += 1
                    history["encounter_count"] = encounter_count
                    logger.info(f"Encuentro #{encounter_count} detectado - variación={delta:.2f}")
                    save_history(history, APP_CONFIG.history_path)

            last_frame = frame

            if detector.detect_shiny(frame):
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                screenshot_path = Path("logs") / f"shiny_{encounter_count}_{int(time.time())}.png"
                screenshot_path.parent.mkdir(parents=True, exist_ok=True)
                save_debug_screenshot(screenshot_path, APP_CONFIG.capture_region)

                event = {
                    "timestamp": timestamp,
                    "encounter_number": encounter_count,
                    "screenshot": str(screenshot_path),
                }
                history.setdefault("shiny_events", []).append(event)
                save_history(history, APP_CONFIG.history_path)

                logger.info(f"¡Shiny detectado en encuentro #{encounter_count}!")
                notify_shiny(
                    encounter_number=encounter_count,
                    screenshot_path=screenshot_path,
                    webhook_url=APP_CONFIG.discord_webhook,
                )
                time.sleep(10)

            time.sleep(APP_CONFIG.poll_interval)

        except KeyboardInterrupt:
            logger.info("Bot detenido por el usuario")
            break
        except Exception as exc:
            logger.exception(f"Error durante la ejecución: {exc}")
            time.sleep(2)


if __name__ == "__main__":
    main()
