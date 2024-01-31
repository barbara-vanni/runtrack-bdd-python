import mysql.connector


class Zoo:
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

    def add_animal(self, nom, race, id_cage, birth_date, pays_origine):
        query ="""
            INSERT INTO animal (nom, race, id_cage, birth_date, pays_origine)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (nom, race, id_cage, birth_date, pays_origine)
        self.cursor.execute(query, values)
        self.db.commit()
    
    def modify_animal(self, animal_id, new_id_cage):
        query = "UPDATE animal SET id_cage = %s WHERE id = %s"
        values = (new_id_cage, animal_id)
        self.cursor.execute(query, values)
        self.db.commit()

    def delete_animal(self, animal_id):
        query = "DELETE FROM animal WHERE id = %s"
        values = (animal_id,)
        self.cursor.execute(query, values)
        self.db.commit()

    def add_cage(self, id, superficie, capacite_max):
        query ="""
            INSERT INTO cage (id, superficie, capacite_max)
            VALUES (%s, %s, %s)
        """
        values = (id, superficie, capacite_max)
        self.cursor.execute(query, values)
        self.db.commit()

    def modify_cage(self, id_cage, new_capacite_max):
        query = "UPDATE cage SET capacite_max = %s WHERE id = %s"
        values = (new_capacite_max, id_cage)
        self.cursor.execute(query, values)
        self.db.commit()
    
    def delete_cage(self, id_cage):
        query = "DELETE FROM cage WHERE id = %s"
        values = (id_cage,)
        self.cursor.execute(query, values)
        self.db.commit()

    def read_all_animal(self):
        query = """
            SELECT animal.nom, animal.race, animal.birth_date, animal.pays_origine, cage.id
            FROM animal
            INNER JOIN cage ON animal.id_cage = cage.id
            """
        self.cursor.execute(query)
        all_animal = self.cursor.fetchall()
        print("\nListe de tous les animaux du zoo:")
        for animal in all_animal:
            nom, race, birth_date, pays_origine, id_cage = animal
            print(f"{nom} : {race}, {birth_date}, {pays_origine}, Cage ID: {id_cage}")

    
    def afficher_animaux_cages(self):
        query = '''
            SELECT cage.id, cage.superficie, cage.capacite_max, GROUP_CONCAT(animal.nom, ', ')
            FROM cage
            LEFT JOIN animal ON cage.id = animal.id_cage
            GROUP BY cage.id
        '''
        self.cursor.execute(query)
        animaux_cages = self.cursor.fetchall()
        for cage in animaux_cages:
            id, superficie, capacite_max, animaux = cage
            print(f"Cage {id} : {superficie}m2, {capacite_max} animaux maximum, {animaux}")

    def calculer_superficie_totale(self):
        self.cursor.execute('SELECT SUM(superficie) FROM cage')
        superficie_totale = self.cursor.fetchall()
        print(f'Superficie totale de toutes les cages : {superficie_totale} m²')

try:
    zoo_animal = Zoo("localhost", "root", "", "zoo")

    # zoo_animal.add_animal('Guépard', 'Félin', 2, '2013-10-27', 'Afrique')
    # zoo_animal.add_cage(1, 100, 1)
    # zoo_animal.add_cage(2, 200, 2)
    # zoo_animal.modify_animal(1, 2)

    zoo_animal.read_all_animal()


    zoo_animal.afficher_animaux_cages()

    zoo_animal.calculer_superficie_totale()
    

    
except Exception as e:
    print(f"Une erreur s'est produite : {e}")

finally:
    zoo_animal.close_connection()
