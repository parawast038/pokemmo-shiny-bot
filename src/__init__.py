from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ASSETS_DIR = ROOT / "assets"
TEMPLATES_DIR = ASSETS_DIR / "templates"
DATA_DIR = ROOT / "data"
LOG_DIR = ROOT / "logs"

TEMPLATE_PATH = TEMPLATES_DIR / "shiny_template.png"
HISTORY_PATH = DATA_DIR / "history.json"
LOG_PATH = LOG_DIR / "shiny_bot.log"
