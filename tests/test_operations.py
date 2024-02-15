'''Test File: operations.py'''
# Disable specific pylint warnings that are not relevant for this file.
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.operations import Operations as op

@pytest.mark.parametrize("operation, a, b, expected", [
    (op.addition, Decimal('2'), Decimal('3'), Decimal('5')),
    (op.addition, Decimal('0.1'), Decimal('0.2'), Decimal('0.3')),
    (op.subtraction, Decimal('5'), Decimal('3'), Decimal('2')),
    (op.subtraction, Decimal('0.3'), Decimal('0.1'), Decimal('0.2')),
    (op.multiplication, Decimal('2'), Decimal('3'), Decimal('6')),
    (op.multiplication, Decimal('0.1'), Decimal('0.2'), Decimal('0.02')),
    (op.division, Decimal('6'), Decimal('3'), Decimal('2')),
    (op.division, Decimal('0.3'), Decimal('0.1'), Decimal('3'))
])

def test_operations(operation, a, b, expected):
    '''Tests various operations with parametrized data'''
    assert operation(a, b) == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_operation_divide_by_zero():
    '''Test case for division by zero'''
    with pytest.raises(ValueError):
        op.division(Decimal('5'), Decimal('0'))
