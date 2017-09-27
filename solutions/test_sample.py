import pytest


def is_even(x):
    """ Checks if number is even
    """
    return x % 2 == 0


# IS EVEN TESTS
def test__two_is_even__succeeds():
    assert is_even(2)


def test__three_is_even__fails():
    assert not is_even(3)


# EXCEPTION TESTING

#  Trying to access a non existent key in a dictionary raises an exception.
#  Write a test for the KeyError exception


def test__dict_no_key__raises():
    some_dict = {'a': 3}
    # code here
    with pytest.raises(KeyError):
        some_dict['b']
