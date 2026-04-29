import os
from datetime import datetime

LOG_FILE = "logs/app.log"

def check_auth() -> bool:
    """
    Symulacja sprawdzenia autoryzacji.
    W prawdziwej aplikacji tutaj byłoby sprawdzenie tokenu/hasła.
    """
    return True

def log_action(message: str) -> None:
    """Zapisuje logi do pliku w folderze logs/."""
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{now}] {message}\n")