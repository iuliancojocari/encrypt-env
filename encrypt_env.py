from cryptography.fernet import Fernet

# Charger la clé
with open("secret.key", "rb") as f:
    key = f.read()

fernet = Fernet(key)

# Lire le .env existant
with open(".env", "rb") as f:
    original_data = f.read()

# Chiffrer
encrypted_data = fernet.encrypt(original_data)

# Sauvegarder la version chiffrée
with open(".env.encrypted", "wb") as f:
    f.write(encrypted_data)

print("Fichier .env chiffré avec succès.")