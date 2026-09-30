import logging
from pathlib import Path


def setup_logger(log_path: str | Path):
    log_file = Path(log_path)
    log_file.parent.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger("pokemmo_shiny_bot")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if logger.handlers:
        return logger

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

    return logger
