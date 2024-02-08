from Database import Db

class Product():
    def __init__(self):
        self.table = 'product'
        self.db = Db(host='localhost', user='root', password='Vcassis13*', database='store')


    def create(self, name, description, price, quantity, id_category):
        query = f'INSERT INTO {self.table} (name, description, price, quantity, id_category ) VALUES (%s, %s, %s, %s, %s)'
        params = (name, description, price, quantity, id_category)
        self.db.executeQuery(query, params)

    def read(self, category=None):
        if category is None:
            query = "SELECT * FROM product"
            return self.db.fetch(query)
        else:
            query = "SELECT * FROM product WHERE id_category = %s"
            params = (category,)
            return self.db.fetch(query, params)
    
    def read_name(self):
        query = f"""SELECT name, price, quantity FROM {self.table}
        """
        for product in self.db.fetch(query):
            name = product[0]
            price = product[1]
            quantity = product[2]
            print(f"{name} {price} {quantity}")
        return self.db.fetch(query)
    


    def display_products(self, screen, font):
        products = self.read_name()
        y_position = 50
        WIDTH = 800

        for product in products:
            product_name = product[0]
            price = product[1]
            quantity = product[2]
            text = font.render(f"{product_name} : {price} : {quantity}", True, 'black')
            text_rect = text.get_rect(center=(WIDTH // 2, y_position))
            screen.blit(text, text_rect)
            y_position += 40

        


    

    def update(self, id, name, price, quantity):
        query = f'UPDATE {self.table} SET name=%s, price=%s, quantity=%s WHERE id=%s'
        params = (name, price, quantity, id)
        self.db.executeQuery(query, params)

    def delete(self, id):
        query = f'DELETE FROM {self.table} WHERE id=%s'
        params = (id)
        self.db.executeQuery(query, params)

    def find(self, id):
        query = f'SELECT * FROM {self.table} WHERE id=%s'
        params = (id)
        return self.db.fetch(query, params)
