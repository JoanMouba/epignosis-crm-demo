# Epignosis CRM Demo

Application web de test pour la formation **Robot Framework Fondations** — Epignosis Center  
Dr.-Ing. Joan Mouba | Formateur accrédité RFCP | [cert.robotframework.org](https://cert.robotframework.org)

---

## Pourquoi cette application ?

Cette app remplace `automationplayground.com/crm` avec :
- Des **données 100 % francophones** : villes, régions et prénoms français
- Un **hébergement sous ton contrôle** : plus de dépendance externe
- Les **mêmes IDs HTML** que l'original → tes fichiers `.robot` existants fonctionnent sans modification (sauf l'URL)

---

## Lancement en local (développement / tournage)

```bash
# 1. Cloner le repo
git clone https://github.com/joanmouba/epignosis-crm-demo.git
cd epignosis-crm-demo

# 2. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Lancer l'application
python app.py
```

L'app démarre sur **http://localhost:5000**

**Identifiants de test :**
- Email : `admin@fakeemail.com`
- Mot de passe : `SecretSauce!25`

---

## Déploiement en ligne (accès apprenants)

### Option A — Render.com (recommandé, gratuit)

1. Créer un compte sur [render.com](https://render.com)
2. New → Web Service → connecter ce repo GitHub
3. Build Command : `pip install -r requirements.txt`
4. Start Command : `gunicorn app:app`
5. Ajouter `gunicorn` dans `requirements.txt`
6. L'app sera accessible sur `https://epignosis-crm.onrender.com`

### Option B — Railway.app (gratuit, plus rapide)

```bash
npm install -g @railway/cli
railway login
railway init
railway up
```

### Option C — Domaine personnalisé

Configurer `demo.epignosiscenter.com` → pointer vers Render/Railway  
→ URL professionnelle pour les screencasts du cours

---

## Adapter tes fichiers Robot Framework

Seul changement nécessaire dans `common_variables.resource` :

```robot
# Avant
${START_URL}    https://automationplayground.com/crm/

# Après (local)
${START_URL}    http://localhost:5000

# Après (en ligne)
${START_URL}    https://demo.epignosiscenter.com
```

Tous les IDs HTML sont identiques à l'original :
`id=email-id`, `id=password`, `id=remember`, `id=submit-id`,
`id=EmailAddress`, `id=FirstName`, `id=LastName`, `id=City`,
`id=StateOrRegion`, `name=promos-name`

---

## Données de test françaises (CSV pour DDT)

Fichier : `rf_resources/customers_fr.csv`

| email | prenom | nom | ville | region | genre | promos |
|-------|--------|-----|-------|--------|-------|--------|
| laura.martin@test.fr | Laura | Martin | Paris | IDF | female | yes |
| jean.dupont@test.fr | Jean | Dupont | Lyon | ARA | male | no |
| emma.petit@test.fr | Emma | Petit | Marseille | PAC | female | yes |
| thomas.leroy@test.fr | Thomas | Leroy | Toulouse | OCC | male | yes |
| camille.moreau@test.fr | Camille | Moreau | Lille | HDF | female | no |

---

## Régions disponibles (select StateOrRegion)

| Code | Région |
|------|--------|
| IDF | Île-de-France |
| ARA | Auvergne-Rhône-Alpes |
| NAQ | Nouvelle-Aquitaine |
| OCC | Occitanie |
| HDF | Hauts-de-France |
| GES | Grand Est |
| PAC | Provence-Alpes-Côte d'Azur |
| PDL | Pays de la Loire |
| NOR | Normandie |
| BRE | Bretagne |
| CVL | Centre-Val de Loire |
| BFC | Bourgogne-Franche-Comté |
| COR | Corse |

---

## Structure du projet

```
epignosis-crm-demo/
├── app.py                      # Application Flask principale
├── requirements.txt            # Dépendances Python
├── crm.db                      # Base SQLite (générée au premier lancement)
├── templates/
│   ├── base.html               # Layout commun (nav, footer)
│   ├── index.html              # Page d'accueil
│   ├── signin.html             # Formulaire de connexion
│   ├── customers.html          # Liste des clients
│   └── new_customer.html       # Formulaire ajout client
└── rf_resources/
    ├── common_variables.resource  # Variables RF (URL, IDs, données test)
    └── customers_fr.csv           # Données DDT françaises
```

---

*Epignosis Center — Formation Robot Framework en français*  
*www.epignosiscenter.podia.com*
