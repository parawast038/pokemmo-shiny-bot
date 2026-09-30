from __future__ import annotations

import logging
from pathlib import Path

import requests
import winsound


def send_discord_webhook(webhook_url: str, message: str, image_path: str | Path | None = None):
    if not webhook_url:
        return False

    payload = {"content": message}
    files = []

    if image_path:
        image_file = Path(image_path)
        if image_file.exists():
            files = [("file", (image_file.name, image_file.read_bytes(), "image/png"))]

    response = requests.post(webhook_url, data=payload, files=files, timeout=10)
    return response.status_code in (200, 204)


def play_windows_alert(frequency: int = 800, duration_ms: int = 600):
    try:
        winsound.Beep(frequency, duration_ms)
    except Exception:
        pass


def notify_shiny(encounter_number: int, screenshot_path: str | Path | None = None, webhook_url: str = ""):
    message = f"¡Shiny detectado! Encuentro #{encounter_number}"
    print(message)
    play_windows_alert()

    if webhook_url:
        send_discord_webhook(webhook_url, message, screenshot_path)

    return message
