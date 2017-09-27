import pytest

# declare skip decorators
skip = pytest.mark.skip
skipif = pytest.mark.skipif
xfail = pytest.mark.xfail


# This is expected to fail
# Mark with xfail
def test_fails():
    """Always fails
    """
    assert 0


# Skip this test
def test_truth():
    """This is always true
    """
    assert True


val = True


def test_skip_if_val_true():
    """Skip this if val is true
    """
    assert 0
