# test_calculator.py

import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0

def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(0, 0) == 0

def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-1, 3) == -3

def test_divide():
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(10, 2) == 5
    assert calculator.divide(0, 5) == 0

def test_divide_by_zero():
    try:
        calculator.divide(5, 0)
    except ValueError as e:
        assert str(e) == "Division by zero is not allowed"
