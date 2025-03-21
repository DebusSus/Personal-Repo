from flask import render_template, Flask
import connexion


app = connexion.FlaskApp(__name__)
app.add_api("api.yml")

@app.route("/")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)