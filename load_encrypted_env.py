from cryptography.fernet import Fernet
from dotenv import load_dotenv
from io import StringIO

def load_encrypted_env(
    encrypted_path=".env.encrypted",
    key_path="secret.key"
):
    """
    Déchiffre un fichier .env chiffré et charge les variables
    dans os.environ sans créer de fichier temporaire.
    """

    # Charger la clé
    with open(key_path, "rb") as f:
        key = f.read()

    fernet = Fernet(key)

    # Lire fichier chiffré
    with open(encrypted_path, "rb") as f:
        encrypted_data = f.read()

    # Déchiffrer
    decrypted_data = fernet.decrypt(encrypted_data).decode()

    # Charger en mémoire uniquement
    load_dotenv(stream=StringIO(decrypted_data))

    # Nettoyage variable sensible en mémoire
    del decrypted_data
