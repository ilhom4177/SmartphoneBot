from db import UserDb, ProductDB

def test_add_user():
    user_db = UserDb()
    user_db.add_user('4324132', 'test', 'test', 'test')

def test_get_brand():
    product_db = ProductDB()
    print(product_db.get_brand())

def get_poroduct_by_brand():
    product_db = ProductDB()
    print(product_db.get_product_by_brand('Apple'))

def test_add_order():
    user_db = UserDb()
    user_db.add_order('3214142', '1233231', 'Apple')

def test_clear_order():
    user_db = UserDb()
    user_db.clear_order('3214142')

def test_get_product():
    product_db = ProductDB()
    print(product_db.get_product('Apple', '1'))

test_get_product()