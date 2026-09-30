from __future__ import annotations

from pathlib import Path
import cv2
import numpy as np


class ShinyDetector:
    def __init__(self, template_path: str | Path, threshold: float = 0.80):
        self.template_path = Path(template_path)
        self.threshold = threshold
        self.template = None

        if self.template_path.exists():
            self.template = cv2.imread(str(self.template_path), cv2.IMREAD_COLOR)

    def has_template(self) -> bool:
        return self.template is not None

    def image_difference(self, image_a, image_b) -> float:
        """Retorna la diferencia de píxeles entre dos imágenes."""
        arr_a = np.array(image_a)
        arr_b = np.array(image_b)
        diff = cv2.absdiff(arr_a, arr_b)
        return float(np.mean(diff))

    def detect_shiny(self, frame) -> bool:
        """Detecta si el frame actual coincide con la plantilla del shiny."""
        if not self.has_template():
            return False

        frame_arr = np.array(frame)
        result = cv2.matchTemplate(frame_arr, self.template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, _ = cv2.minMaxLoc(result)
        return bool(max_val >= self.threshold)
