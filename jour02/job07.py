import mysql.connector

# ----------------------------------------------- 1ere partie du job ---------------------------------------
# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Vcassis13*",
#     database="entreprise"
# )




# cursor = db.cursor()

# join = """
#     SELECT employe.nom, employe.prenom, service.nom
#     FROM employe 
#     INNER JOIN service ON employe.id_service = service.id
# """

# cursor.execute(join)
# employe_service = cursor.fetchall()

# for employes in employe_service:
#     nom, prenom, nom_service = employes

#     print(f"{nom} {prenom} travaille au service {nom_service}")

# cursor.close()
# db.close()

# ----------------------------------------------- 2eme partie du job ---------------------------------------




class Employe:
    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.db.cursor()

    def close_connection(self):
        self.db.close()
        self.cursor.close()

    # def get_all_employees_with_service(self):
    #     query = """
    #         SELECT employe.nom, employe.prenom, service.nom
    #         FROM employe 
    #         INNER JOIN service ON employe.id_service = service.id
    #     """
    #     self.cursor.execute(query)
    #     employe_service = self.cursor.fetchall()
    #     return employe_service

    def create_employe(self, nom, prenom, salaire, id_service):
        query ="""
            INSERT INTO employe (nom, prenom, salaire, id_service)
            VALUES (%s, %s, %s, %s)
        """
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.db.commit()

    def read_employe(self):
        query = """
            SELECT employe.nom, employe.prenom, employe.salaire, service.nom
            FROM employe
            INNER JOIN service ON employe.id_service = service.id
            """
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def update_employe(self, employe_id, new_salaire):
        query = "UPDATE employe SET salaire = %s WHERE id = %s"
        values = (new_salaire, employe_id)
        self.cursor.execute(query, values)
        self.db.commit()

    def delete_employe(self, employe_id):
        query = "DELETE FROM employe WHERE id = %s"
        values = (employe_id,)
        self.cursor.execute(query, values)
        self.db.commit()




employe_instance = Employe("localhost", "root", "Vcassis13*", "entreprise")


employe_instance.create_employe("New", "New", 2500.50, 2)
employe_instance.delete_employe(10)



all_employe_data = employe_instance.read_employe()
print("\nListe de tous les salariés :")
for employe in all_employe_data:
    nom, prenom, salaire, service = employe
    print(f"{nom} {prenom} gagne {salaire} au service {service}")


employe_instance.update_employe(1, 2000000)


employe_instance.close_connection()
