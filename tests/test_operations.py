'''Test File: operations.py'''
# Disable specific pylint warnings that are not relevant for this file.
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from calculator.operations import Operations as op

def test_operations(a, b, operation, expected):
    '''Tests various operations with parametrized data'''
    assert operation(a, b) == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def test_operation_divide_by_zero():
    '''Test case for division by zero'''
    with pytest.raises(ValueError):
        op.division(Decimal('5'), Decimal('0'))
