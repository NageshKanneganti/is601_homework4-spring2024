'''Test File: __init__.py'''
# Disable specific pylint warnings that are not relevant for this file.
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator import Calculator

@pytest.mark.parametrize("calculator_op, a, b, expected", [
    (Calculator.add, Decimal('2'), Decimal('2'), Decimal('4')),
    (Calculator.subtract, Decimal('2'), Decimal('2'), Decimal('0')),
    (Calculator.multiply, Decimal('2'), Decimal('2'), Decimal('4')),
    (Calculator.divide, Decimal('2'), Decimal('2'), Decimal('1')),
    (Calculator.add, Decimal('1.0'), Decimal('2.0'), Decimal('3.0')),
    (Calculator.subtract, Decimal('3.0'), Decimal('2.0'), Decimal('1.0')),
    (Calculator.multiply, Decimal('2.0'), Decimal('3.0'), Decimal('6.0')),
    (Calculator.divide, Decimal('6.0'), Decimal('2.0'), Decimal('3.0')),
])

def test_calculator_operations(calculator_op, a, b, expected):
    '''Test Calculator class operations'''
    assert calculator_op(a, b) == expected, f"Failed {calculator_op.__name__} operation with {a} and {b}"

def test_calculator_divide_by_zero():
    '''Test calculator divide by zero exception'''
    with pytest.raises(ValueError):
        Calculator.divide(2, 0)
