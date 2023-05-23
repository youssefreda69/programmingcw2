from flask import Flask, render_template, request, redirect, session
import secrets

app = Flask(__name__)
app.secret_key = "password"  


users = [
    {"username": "user1", "password": "password1"},
    {"username": "user2", "password": "password2"},
    {"username": "user3", "password": "password3"}
]

# Generate a random client ID and client secret
client_id = secrets.token_urlsafe(16)
client_secret = secrets.token_urlsafe(32)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Check if the username and password are valid
        for user in users:
            if user["username"] == username and user["password"] == password:
                # Successful login
                session["username"] = username
                return redirect("/dashboard")

        # Invalid credentials
        return render_template("client_login.html", error="Invalid username or password")

    return render_template("client_login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Check if the username is already taken
        for user in users:
            if user["username"] == username:
                return render_template("client_register.html", error="Username already taken")

        # Register the new user
        users.append({"username": username, "password": password})
        return redirect("/login")

    return render_template("client_register.html")

@app.route("/dashboard")
def dashboard():
    if "username" in session:
        username = session["username"]
        return render_template("auth_dashboard.html", welcome_message=f"Welcome, {username}!", client_id=client_id, client_secret=client_secret)
    else:
        return redirect("/login")

@app.route("/redirect-to-shopping-app")
def redirect_to_shopping_app():
    return redirect("http://localhost:5000/dashboard")  # Redirect to the shopping app dashboard

if __name__ == "__main__":
    app.run(port=8000, debug=True)
