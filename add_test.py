import pytest
from add import add

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 4, 4),
    (7, 0, 7),
    (-2, 0, -2),
    (0, -13, -13),
])
def test_add(a, b, expected):
    got = add(a, b)
    assert got == expected, f"{expected=}, {got=}"