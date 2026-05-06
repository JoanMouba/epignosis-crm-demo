# Guide de déploiement — Epignosis CRM Demo

## Déploiement local (Windows)

```bash
# 1. Extraire le zip
# 2. Ouvrir un terminal dans le dossier

# 3. Créer un environnement virtuel
python -m venv venv
venv\Scripts\activate

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Lancer l'application
python app.py
```

L'app démarre sur **http://localhost:5000**

Identifiants : admin@fakeemail.com / SecretSauce!25

---

## Déploiement sur Render.com (gratuit)

### Pré-requis
- Compte GitHub
- Compte Render.com (gratuit)

### Étapes

1. Créer un repo GitHub public avec ce code
2. Sur Render.com → New → Web Service
3. Connecter le repo GitHub
4. Render détecte automatiquement render.yaml
5. Cliquer Deploy

L'app sera accessible sur :
**https://epignosis-crm-demo.onrender.com**

### Variables d'environnement (auto-générées par render.yaml)
- SECRET_KEY : généré automatiquement

---

## Note sur Netlify

Netlify ne supporte pas Flask nativement.
Utiliser Render.com comme recommandé.

---

## URL personnalisée (optionnelle)

Sur Render.com → Settings → Custom Domain
Ajouter : demo.epignosiscenter.com
Pointer votre DNS : CNAME → epignosis-crm-demo.onrender.com
