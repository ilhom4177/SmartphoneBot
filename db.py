from tinydb import TinyDB, Query


class UserDb:
    def __init__(self):
        user_db = TinyDB('db/user.json', indent=4)
        self.user_table = user_db.table('User')
        self.order_table = user_db.table('Order')
        self.query = Query()

    def add_user(self, chat_id: str, first_name:str, username=None, last_name=None):
        user = {
            'chat_id': chat_id,
            'first_name': first_name,
            'username': username,
            'last_name': last_name
        }
        if self.user_table.contains(self.query.chat_id == chat_id):
            return self.user_table.update(user, self.query.chat_id == chat_id)
        return self.user_table.insert(user)
    
    def add_order(self, chat_id: str, product_id: str, company: str):
        if self.order_table.contains((self.query.chat_id == chat_id) & (self.query.company == company) & (self.query.product_id == product_id)):
            order = self.order_table.get((self.query.chat_id == chat_id) & (self.query.company == company) & (self.query.product_id == product_id))
            order['quantity'] += 1
            return self.order_table.update(order, (self.query.chat_id == chat_id) & (self.query.company == company) & (self.query.product_id == product_id))
        
        order = {
            'chat_id': chat_id,
            'product_id': product_id,
            'company': company,
            'quantity': 1
        }
        return self.order_table.insert(order)
    
class ProductDB:
    def __init__(self) -> None:
        self.db = TinyDB('db/product.json', indent=4)
        self.query = Query()
    
    def get_brand(self):
        return self.db.tables()

    def get_product_by_brand(self, brand):
        table = self.db.table(brand)
        return table.all()
    