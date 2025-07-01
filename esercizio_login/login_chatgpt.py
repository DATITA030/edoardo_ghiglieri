class LoginError(Exception):
    """Classe base per errori di login"""
    pass

class UsernameNotFoundError(LoginError):
    """Errore quando l'username non è presente"""
    pass

class IncorrectPasswordError(LoginError):
    """Errore quando la password è sbagliata"""
    pass

class TooManyAttemptsError(LoginError):
    """Errore quando si superano i tentativi consentiti"""
    pass

# === Funzione di login ===

def login(utenti, max_tentativi=3):
    tentativi = 0

    while tentativi < max_tentativi:
        username = input("Nome utente: ")
        password = input("Password: ")

        try:
            if username not in utenti:
                raise UsernameNotFoundError("⚠️ Username non trovato.")
            if utenti[username] != password:
                raise IncorrectPasswordError("⚠️ Password errata.")

            print(f"✅ Accesso riuscito! Benvenuto, {username}.")
            return True

        except LoginError as e:
            tentativi += 1
            print(e)
            print(f"Tentativi rimasti: {max_tentativi - tentativi}\n")

    raise TooManyAttemptsError("🚫 Troppi tentativi falliti. Accesso bloccato.")


# === Utenti registrati ===

utenti = {
    "admin": "1234",
    "mario": "ciao123",
    "luigi": "password"
}

# === Avvio del programma ===

try:
    login(utenti)
except TooManyAttemptsError as e:
    print(e)