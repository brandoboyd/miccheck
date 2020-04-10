import pytest

class Calculator:
    """A terrible calculator"""

    def add (self, a, b):
        return a + b

    def subtract (self, a, b):
        return a - b

def test_add():
    calculator = Calculator()

    result = calculator.add(2, 3)

    assert result == 5

def test_subtract():
    calculator = Calculator()

    result = calculator.subtract(10, 5)

    assert result == 5   
