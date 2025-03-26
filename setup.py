import mysql.connector

my_db = mysql.connector.connect(
    user="root",
    password="4562",
    host="127.0.0.1",
    database="players"
)

pointer = my_db.cursor()

pointer.execute("SHOW TABLES LIKE 'player_credentials'")
answer = pointer.fetchone()

if not answer:
    print("Table 'player_credentials' doesnt exist, lets make one!")
    try:
        pointer.execute("""
            CREATE TABLE player_credentials (
                id int NOT NULL AUTO_INCREMENT,
                name varchar(25) NOT NULL,
                email varchar(50) NOT NULL,
                fave_warframe varchar(25),
                PRIMARY KEY (id)
            )
        """)
        print("Yay! The 'player_credentials' table is ready!")
        my_db.commit()
    except Exception as oops:
        print("Uh oh, something went wrong:", oops)
        exit(1)

try:
    add_player = ("INSERT INTO player_credentials "
                  "(name, email, fave_warframe) "
                  "VALUES (%s, %s, %s)")
    
    pointer.execute(add_player, ("Gary", "garyandrew@yahoo.com", "Atlas"))
    pointer.execute(add_player, ("New_Player", "nottellingumynam3@hotmail.net", "Excalibur"))
    pointer.execute(add_player, ("Proud_Father", "veryproudfather@gmail.com", "Gauss"))
    
    my_db.commit()

except Exception as oops:
    print("Inserting failed for the following reason: ", oops)

query = ("SELECT * FROM player_credentials")

pointer.execute(query)

for (id, name, email, fave_warframe) in pointer:
    print("Player:", name, "(id:", id, ")")
    print("Email:", email)
    print("Favourite Warframe:", fave_warframe)
    print()

pointer.close()
my_db.close()