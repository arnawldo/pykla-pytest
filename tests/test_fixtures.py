import pytest

class UserDB(object):
    """Custom database for users
    Attributes:
        users -- names of users stored
        number -- number of users stored
    """
    def __init__(self):
        self.users = []
        self.number = 0
    def add_user(self, name):
        """Add user to db"""
        self.users.append(name)
        self.number += 1
    def remove_user(self, name):
        self.users.remove(name)
        self.number -= 1

@pytest.fixture
def user_db():
    """Custom database for users
    """
    db = UserDB()
    return db


def test_has_no_users_db(user_db):
    """Test that number of users is zero"""
    assert 0


def test_can_add_user_db(user_db):
    """Test that db can add a user"""
    assert 0


def test_can_remove_user_db(user_db):
    """Test that db can remove a user"""
    assert 0
