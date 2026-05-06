from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3, os

app = Flask(__name__)
import os
app.secret_key = os.environ.get("SECRET_KEY", "epignosis-crm-secret-dev-2026")
DB = os.path.join(os.path.dirname(__file__), "crm.db")

VALID_EMAIL    = "admin@fakeemail.com"
VALID_PASSWORD = "SecretSauce!25"

REGIONS = [
    ("", "-- Sélectionnez une région --"),
    ("IDF", "Île-de-France"),
    ("ARA", "Auvergne-Rhône-Alpes"),
    ("NAQ", "Nouvelle-Aquitaine"),
    ("OCC", "Occitanie"),
    ("HDF", "Hauts-de-France"),
    ("GES", "Grand Est"),
    ("PAC", "Provence-Alpes-Côte d'Azur"),
    ("PDL", "Pays de la Loire"),
    ("NOR", "Normandie"),
    ("BRE", "Bretagne"),
    ("CVL", "Centre-Val de Loire"),
    ("BFC", "Bourgogne-Franche-Comté"),
    ("COR", "Corse"),
]

def get_db():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id        INTEGER PRIMARY KEY AUTOINCREMENT,
                email     TEXT NOT NULL,
                firstname TEXT NOT NULL,
                lastname  TEXT NOT NULL,
                city      TEXT NOT NULL,
                region    TEXT NOT NULL,
                gender    TEXT NOT NULL,
                promos    INTEGER NOT NULL DEFAULT 0
            )
        """)
        conn.execute("DELETE FROM customers")
        seed = [
            ("marie.dupont@email.fr",   "Marie",   "Dupont",   "Paris",         "IDF", "female", 1),
            ("thomas.martin@email.fr",  "Thomas",  "Martin",   "Lyon",          "ARA", "male",   0),
            ("sophie.bernard@email.fr", "Sophie",  "Bernard",  "Bordeaux",      "NAQ", "female", 1),
            ("lucas.petit@email.fr",    "Lucas",   "Petit",    "Toulouse",      "OCC", "male",   1),
            ("camille.moreau@email.fr", "Camille", "Moreau",   "Lille",         "HDF", "female", 0),
            ("Antoine.leroy@email.fr",  "Antoine", "Leroy",    "Strasbourg",    "GES", "male",   1),
            ("emma.simon@email.fr",     "Emma",    "Simon",    "Marseille",     "PAC", "female", 1),
            ("noah.laurent@email.fr",   "Noah",    "Laurent",  "Nantes",        "PDL", "male",   0),
        ]
        conn.executemany(
            "INSERT INTO customers (email,firstname,lastname,city,region,gender,promos) VALUES (?,?,?,?,?,?,?)",
            seed
        )
        conn.commit()

# ── Pages publiques ────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["GET", "POST"])
def signin():
    error = None
    if request.method == "POST":
        email    = request.form.get("email-id", "")
        password = request.form.get("password", "")
        if email == VALID_EMAIL and password == VALID_PASSWORD:
            session["logged_in"] = True
            session["email"]     = email
            return redirect(url_for("customers"))
        else:
            error = "Invalid Login Credentials"
    return render_template("signin.html", error=error)

@app.route("/signout")
def signout():
    session.clear()
    return redirect(url_for("index"))

# ── Pages protégées ───────────────────────────────────────────────

@app.route("/customers")
def customers():
    if not session.get("logged_in"):
        return redirect(url_for("signin"))
    with get_db() as conn:
        rows = conn.execute("SELECT * FROM customers ORDER BY id DESC").fetchall()
    return render_template("customers.html", customers=rows)

@app.route("/new-customer", methods=["GET", "POST"])
def new_customer():
    if not session.get("logged_in"):
        return redirect(url_for("signin"))

    success = False
    error   = None

    if request.method == "POST":
        email     = request.form.get("EmailAddress", "").strip()
        firstname = request.form.get("FirstName", "").strip()
        lastname  = request.form.get("LastName", "").strip()
        city      = request.form.get("City", "").strip()
        region    = request.form.get("StateOrRegion", "").strip()
        gender    = request.form.get("gender", "").strip()
        promos    = 1 if request.form.get("promos-name") else 0

        if not all([email, firstname, lastname, city, region, gender]):
            error = "Tous les champs obligatoires doivent être remplis."
        else:
            with get_db() as conn:
                existing = conn.execute(
                    "SELECT id FROM customers WHERE email=?", (email,)
                ).fetchone()
                if existing:
                    error = "Un client avec cet email existe déjà."
                else:
                    conn.execute(
                        "INSERT INTO customers (email,firstname,lastname,city,region,gender,promos) VALUES (?,?,?,?,?,?,?)",
                        (email, firstname, lastname, city, region, gender, promos)
                    )
                    conn.commit()
                    success = True

    return render_template("new_customer.html", regions=REGIONS, success=success, error=error)

@app.route("/delete-customer/<int:cid>", methods=["POST"])
def delete_customer(cid):
    if not session.get("logged_in"):
        return redirect(url_for("signin"))
    with get_db() as conn:
        conn.execute("DELETE FROM customers WHERE id=?", (cid,))
        conn.commit()
    return redirect(url_for("customers"))

# ── Lancement ─────────────────────────────────────────────────────

# Initialisation DB au démarrage (fonctionne avec gunicorn ET python app.py)
with app.app_context():
    init_db()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)