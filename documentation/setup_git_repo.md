Quick setup — if you’ve done this kind of thing before

Get started by creating a new file or uploading an existing file. We recommend every repository include a README, LICENSE, and .gitignore.

--
https: https://github.com/JoanMouba/epignosis-crm-demo.git
ssh: git@github.com:JoanMouba/epignosis-crm-demo.git
--
…or create a new repository on the command line
echo "# epignosis-crm-demo" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/JoanMouba/epignosis-crm-demo.git
git push -u origin main

--
…or push an existing repository from the command line
git remote add origin https://github.com/JoanMouba/epignosis-crm-demo.git
git branch -M main
git push -u origin main

--- Structure du repo ---
epignosis_crm/
├── app.py              ← fonctionne local ET Render
├── requirements.txt    ← flask + gunicorn
├── Procfile            ← utilisé par Render uniquement (ignoré en local)
├── render.yaml         ← utilisé par Render uniquement (ignoré en local)
├── .gitignore          ← utilisé par GitHub uniquement (ignoré en local)
├── templates/          ← identique local et Render
└── rf_resources/       ← identique local et Render

--- Pour démarrer en local maintenant ---
# 1. Extraire le zip
# 2. Ouvrir un terminal dans le dossier epignosis_crm/

python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
