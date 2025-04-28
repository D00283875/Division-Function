import pytest
from Division import division

@pytest.mark.parametrize("a,b,expected", [(4, 2, 2), (6, 3, 2), (6, 0, -1)])
def test_division(a, b, expected):
    assert division(a, b) == expected
