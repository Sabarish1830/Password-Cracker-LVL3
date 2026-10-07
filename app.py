from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "cybersecurity_secret_key"

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cybersecurity_db"
)


@app.route("/")
def home():
    return redirect(url_for("login"))


# REGISTER
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if len(username) < 3 or len(password) < 6:
            return "Username must be 3+ characters and password 6+ characters"

        hashed_password = generate_password_hash(password)

        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, hashed_password)
        )

        db.commit()
        cursor.close()

        return redirect(url_for("login"))

    return render_template("register.html")


# LOGIN
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        cursor = db.cursor(dictionary=True)

        cursor.execute(
            "SELECT * FROM users WHERE username = %s",
            (username,)
        )

        user = cursor.fetchone()
        cursor.close()

        if user and check_password_hash(user["password"], password):

            session["username"] = username

            return redirect(url_for("dashboard"))

        return "Invalid Username or Password"

    return render_template("login.html")


# DASHBOARD
@app.route("/dashboard")
def dashboard():

    if "username" not in session:
        return redirect(url_for("login"))

    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM incidents ORDER BY id DESC")

    incidents = cursor.fetchall()

    cursor.close()

    return render_template(
        "dashboard.html",
        username=session["username"],
        incidents=incidents
    )


# ADD INCIDENT
@app.route("/add_incident", methods=["GET", "POST"])
def add_incident():

    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]
        severity = request.form["severity"]
        status = request.form["status"]

        if not title or not description:
            return "Title and Description are required"

        cursor = db.cursor()

        cursor.execute(
            """
            INSERT INTO incidents
            (title, description, severity, status, reported_by)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (
                title,
                description,
                severity,
                status,
                session["username"]
            )
        )

        db.commit()
        cursor.close()

        return redirect(url_for("dashboard"))

    return render_template("add_incident.html")

@app.route("/add_incident", methods=["GET", "POST"])
def add_incident():

    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":

        title = request.form["title"]
        description = request.form["description"]
        severity = request.form["severity"]
        status = request.form["status"]

        if not title or not description:
            return "Title and Description are required"

        cursor = db.cursor()

        cursor.execute(
            """
            INSERT INTO incidents
            (title, description, severity, status, reported_by)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (title, description, severity, status, session["username"])
        )

        db.commit()
        cursor.close()

        return redirect(url_for("dashboard"))

    return render_template("add_incident.html")
# LOGOUT
@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)