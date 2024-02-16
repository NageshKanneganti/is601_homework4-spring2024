'''Test File: __init__.py'''
# Disable specific pylint warnings that are not relevant for this file.
# pylint: disable=unnecessary-dunder-call, invalid-name
import pytest
from calculator import Calculator

def test_addition():
    '''Test that calculator add function works '''    
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Test that calculator subtract function works '''    
    assert Calculator.subtract(2,2) == 0

def test_multiply():
    '''Test that calculator multiply function works '''    
    assert Calculator.multiply(2,2) == 4

def test_divide():
    '''Test that calculator divide function works '''    
    assert Calculator.divide(2,2) == 1

def test_calculator_divide_by_zero():
    '''Test calculator divide by zero exception'''
    with pytest.raises(ValueError):
        Calculator.divide(2, 0)
