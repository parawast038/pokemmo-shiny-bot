from __future__ import annotations

from pathlib import Path
import time

import pyautogui


def capture_region(region: tuple[int, int, int, int] | None = None):
    """Captura una región de la pantalla.

    La tupla es (x, y, width, height).
    """
    if region is None:
        return pyautogui.screenshot()
    return pyautogui.screenshot(region=region)


def save_debug_screenshot(path: str | Path, region: tuple[int, int, int, int] | None = None):
    image = capture_region(region)
    image.save(path)
    return str(path)


def wait_for_window(window_name: str = "PokéMMO"):
    """Espera a que la ventana del juego aparezca en la parte superior."""
    while True:
        try:
            pyautogui.getWindowsWithTitle(window_name)
            time.sleep(1)
            return True
        except Exception:
            time.sleep(1)
