from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "password"  

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login_auth():
    username = request.form.get("username")
    password = request.form.get("password")

    

    return redirect("/dashboard")

@app.route("/authenticator-login")
def authenticator_login():
    

    return redirect("http://localhost:8000/login")  # Redirect to the authorization app login page

@app.route("/dashboard")
def dashboard():
    if "username" in session:
        username = session["username"]
        return render_template("shop_dashboard.html", welcome_message=f"Welcome, {username}!")
    else:
        return redirect("/login")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
