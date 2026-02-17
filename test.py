import os
from load_encrypted_env import load_encrypted_env

load_encrypted_env()

print(os.getenv("PASSWORD"))