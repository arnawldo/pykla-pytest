import pytest


def is_even(number):
    return number % 2 == 0


def sum_is_even(a, b):
    return (a + b) % 2 == 0


# use parametrization to test multiple numbers with one test
def test_is_even():
    assert is_even(2)


def test_sum_is_even():
    assert sum_is_even(1, 5)
