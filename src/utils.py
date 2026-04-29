import hashlib
import logging
import os

os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename='logs/app.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    encoding='utf-8'
)

def log_action(action):
    logging.info(action)

def check_auth():
    pass_path = "data/.pass"
    if not os.path.exists(pass_path):
        print("Pierwsze uruchomienie: Ustaw hasło główne.")
        password = input("Wpisz nowe hasło: ")
        with open(pass_path, "w") as f:
            f.write(hashlib.sha256(password.encode()).hexdigest())
        return True
q
    attempt = input("Wpisz hasło dostępu: ")
    hashed_attempt = hashlib.sha256(attempt.encode()).hexdigest()
    
    with open(pass_path, "r") as f:
        if f.read() == hashed_attempt:
            return True
        print("Błąd: Nieprawidłowe hasło!")
        return False