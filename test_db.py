from db import UserDb

def test_add_user():
    user_db = UserDb()
    user_db.add_user('4324132', 'test', 'test', 'test')

test_add_user()