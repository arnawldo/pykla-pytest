import pytest


def is_even(number):
    return number % 2 == 0


def sum_is_even(a, b):
    return (a + b) % 2 == 0


# use parametrization to test multiple numbers with one test
@pytest.mark.parametrize("x", [2, 4, 6, 8])
def test_is_even(x):
    assert is_even(x)


@pytest.mark.parametrize("a, b", [(7, 7), (2, 2), (3, 7)])
def test_sum_is_even(a, b):
    assert sum_is_even(a, b)