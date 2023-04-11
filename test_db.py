from db import UserDb, ProductDB

def test_add_user():
    user_db = UserDb()
    user_db.add_user('4324132', 'test', 'test', 'test')

def test_get_brand():
    product_db = ProductDB()
    print(product_db.get_brand())

test_get_brand()