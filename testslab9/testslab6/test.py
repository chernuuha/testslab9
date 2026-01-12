import pytest
from Calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
    (10, -5, 5),
    (3.14, 2.86, 6.0),
])
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (9, 3, 3.0),
    (7, 2, 3.5),
    (-10, 2, -5.0),
    (0, 1, 0.0),
])
def test_divide_normal(calc, a, b, expected):
    assert calc.divide(a, b) == expected

def test_divide_by_zero(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(10, 0)

@pytest.mark.parametrize("n, expected", [
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (25, False),
    (1, False),
    (0, False),
    (-5, False),
    (97, True),
    (100, False),
])
def test_is_prime_number(calc, n, expected):
    assert calc.is_prime_number(n) == expected