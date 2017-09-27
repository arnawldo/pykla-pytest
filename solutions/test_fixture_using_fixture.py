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

# Create a second fixture user_db_with_foo that has already added a user "Foo"

@pytest.fixture
def user_db_with_foo(user_db):
    """Custom database for users with
    User 'Foo' included
    """
    user_db.add_user('Foo')
    return user_db


def test_has_no_users_db(user_db):
    """Test that number of users is zero"""
    assert user_db.number == 0


def test_has_one_user_db(user_db_with_foo):
    """Test that db contains user 'Foo'"""
    assert user_db_with_foo.number == 1


def test_can_remove_user_db(user_db_with_foo):
    """Test that db can remove a user"""
    user_db_with_foo.remove_user("Foo")
    assert user_db_with_foo.number == 0
