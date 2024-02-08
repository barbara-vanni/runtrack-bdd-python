from Database import Db
from Product import Product
from Category import Category

class Shop():
    def __init__(self) -> None:
        self.product = Product()
        self.category = Category()  


    def create_Product(self, name, description, price, quantity, id_category):
        self.product.create(name, description, price, quantity, id_category)
    

    def read_Product(self, category=None):
        return self.product.read(category)
    
    def read_Product_name(self):
        return self.product.read_name()
    
    def display_products(self, screen, font):
        self.product.display_products(screen, font)

    def display_category(self, screen, font):
        self.category.display_category(screen, font)
    
    def update_Product(self, id,name, price, quantity):
        self.product.update(id,name, price, quantity)

    def delete_Product(self, id):
        self.product.delete((id,))

    def find_Product(self, id):
        return self.product.find((id,))
    
    def create_Category(self, name):
        self.category.create(name)

    def read_Category(self):
        return self.category.read()
    
    def update_Category(self, id, name):
        self.category.update(id, name)
    
    def delete_Category(self, id):
        self.category.delete(id)
    
    def find_Category(self, id):
        return self.category.find(id)
    
    def find_Product_by_Category(self, id_category):
        query = f'SELECT * FROM {self.product.table} WHERE id_category=%s'
        params = (id_category,)
        return self.product.db.fetch(query, params)
    
    def find_Category_by_Product(self, id_product):
        query = f'SELECT * FROM {self.category.table} WHERE id=%s'
        params = (id_product,)
        return self.category.db.fetch(query, params)
    
