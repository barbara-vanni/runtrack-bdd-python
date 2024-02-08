from Database import Db

class Category ():
    def __init__(self):
        self.table = 'category'
        self.db = Db(host='localhost', user='root', password='Vcassis13*', database='store')


    def create(self, name):
        query = f'INSERT INTO {self.table} (name) VALUES (%s)'
        params = (name)
        self.db.executeQuery(query, params)

    def read(self):
        query = f'SELECT * FROM {self.table}'
        return self.db.fetch(query)
    
    def display_category(self, screen, font):
        category = self.read()
        y_position = 50
        WIDTH = 800

        for category in category:
            category_name = category[1]
            text = font.render(f"{category_name}", True, 'black')
            text_rect = text.get_rect(center=(WIDTH // 2, y_position))
            screen.blit(text, text_rect)
            y_position += 40
    
    def update(self, id, name):
        query = f'UPDATE {self.table} SET name=%s WHERE id=%s'
        params = (name, id)
        self.db.executeQuery(query, params)

    def delete(self, id):
        query = f'DELETE FROM {self.table} WHERE id=%s'
        params = (id,)
        self.db.executeQuery(query, params)
    
    def find(self, id):
        query = f'SELECT * FROM {self.table} WHERE id=%s'
        params = (id,)
        return self.db.fetch(query, params)
    
    