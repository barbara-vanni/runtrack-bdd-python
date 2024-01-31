import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="LaPlateforme"
)


cursor = db.cursor()
cursor.execute("SELECT SUM(capacite) FROM salle")
capacite_salle = cursor.fetchone()[0]

print(f"La capacité de toutes les salles est de {capacite_salle}")

cursor.close()
db.close()