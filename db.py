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
        