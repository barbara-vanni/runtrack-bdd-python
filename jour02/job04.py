import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vcassis13*",
    database="LaPlateforme"
)

cursor = db.cursor()
cursor.execute("SELECT nom, capacite FROM `LaPlateforme`.salle")
result = cursor.fetchall()
print(result)

cursor.close()
db.close()