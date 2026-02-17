# 🔐 Sécurisation du fichier `.env` avec chiffrement

Ce projet utilise un fichier `.env` chiffré pour protéger les **variables sensibles** comme les clés API, mots de passe ou secrets d'application. Cette méthode permet de séparer le code et les secrets tout en assurant leur sécurité.

---

## 1️⃣ Pré-requis

Avant toute manipulation :

- Installer les dépendances Python pour le chiffrement et la gestion des variables d’environnement.
- Utiliser un environnement virtuel pour isoler le projet.

---

## 2️⃣ Génération de la clé de chiffrement

- Une clé de chiffrement est nécessaire pour sécuriser le fichier `.env` -> fichier generate_key.py
- Elle doit être **générée une seule fois** et stockée en lieu sûr.
- **Ne jamais versionner cette clé** dans Git.
- Ajouter le fichier de clé et le `.env` original au `.gitignore`.

---

## 3️⃣ Chiffrement du fichier `.env`

- Le fichier `.env` existant est lu et chiffré pour créer un fichier sécurisé (`.env.encrypted`) -> fichier encrypt_env.py
- Après vérification, le fichier `.env` original doit être supprimé pour éviter toute fuite.
- Le fichier chiffré peut être versionné dans le dépôt Git, car il est illisible sans la clé.

---

## 4️⃣ Déchiffrement et chargement sécurisé

- Une fonction dédiée déchiffre le fichier chiffré et charge les variables **uniquement en mémoire** -> fichier load_encrypted_env.py
- Les variables sont disponibles dans l’environnement du processus Python mais **ne sont jamais écrites en clair sur le disque**.
- Cette approche protège les secrets même si le serveur ou l’environnement de développement est compromis.

---

