from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

ALLOWED_WARFRAMES = [
    "Ash", "Atlas", "Banshee", "Baruuk", "Caliban", "Chroma", "Citrine", "Cyte-09", "Dagath", "Dante",
    "Ember", "Equinox", "Excalibur", "Frost", "Gara", "Garuda", "Gauss", "Grendel", "Gyre", "Harrow",
    "Hildryn", "Hydroid", "Inaros", "Ivara", "Jade", "Khora", "Koumei", "Kullervo", "Lavos", "Limbo",
    "Loki", "Mag", "Mesa", "Mirage", "Nekros", "Nezha", "Nidus", "Nova", "Nyx", "Oberon", "Octavia",
    "Protea", "Qorvex", "Revenant", "Rhino", "Saryn", "Sevagoth", "Styanax", "Temple", "Titania",
    "Trinity", "Valkyr", "Vauban", "Volt", "Voruna", "Wisp", "Wukong", "Xaku", "Yareli", "Zephyr"
]

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        fave_warframe = request.form['fave_warframe']

        if fave_warframe and fave_warframe not in ALLOWED_WARFRAMES:
            return "Error: Invalid Warframe name. Please select a valid Warframe from the list."

        try:
            cnx = mysql.connector.connect(user='root', password='4562',
                                          host='127.0.0.1', database='players')
            cursor = cnx.cursor()

            add_player = ("INSERT INTO player_credentials "
                          "(name, email, fave_warframe) "
                          "VALUES (%s, %s, %s)")
            
            cursor.execute(add_player, (name, email, fave_warframe or None))

            cnx.commit()
            cursor.close()
            cnx.close()
            
        except Exception as error:
            print(error)
            print("Inserting failed for the reason above here")
            return "Registration failed: " + str(error)

        return "Player registered successfully! <a href='/'>Register another player</a>"

    return render_template('register.html', warframes=ALLOWED_WARFRAMES)

app.run(port=80, host='0.0.0.0')