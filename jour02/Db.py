import mysql.connector

class DB:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )


    def create_table(self, table_name, columns):
        self.cursor = self.connection.cursor()
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns)})"
        self.cursor.execute(query)
        self.connection.commit()

    def insert_data(self, table_name, data):
        self.cursor = self.connection.cursor()
        columns = ', '.join(data.keys())
        values = ', '.join([f"'{value}'" for value in data.values()])
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
        self.cursor.execute(query)
        self.connection.commit()

    def read_table(self, table_name, condition=None):
        self.cursor = self.connection.cursor()
        query = f"SELECT * FROM {table_name}"
        if condition:
            query += f" WHERE {condition}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def update_data(self, table_name, data, condition):
        self.cursor = self.connection.cursor()
        update_values = ', '.join([f"{key} = '{value}'" for key, value in data.items()])
        query = f"UPDATE {table_name} SET {update_values} WHERE {condition}"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_data(self, table_name, condition):
        self.cursor = self.connection.cursor()
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(query)
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()



# db.insert_data("exemple_table", {"nom": "John Doe", "age": 25})


# result = db.read_table("exemple_table")
# print(result)

# db.update_data("exemple_table", {"age": 26}, "nom = 'John Doe'")


# db.delete_data("exemple_table", "nom = 'John Doe'")


