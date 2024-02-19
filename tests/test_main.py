'''File Test: main.py'''
# Disable specific pylint warnings that are not relevant for this file.
# pylint: disable=unnecessary-dunder-call, invalid-name
import sys
import pytest
from main import calculate_and_print, main, SYMBOL_TO_OPERATION

# Test mapping of symbols to operation names
def test_main_symbol_to_operation_mapping():
    '''Test mapping of symbol to operation name'''
    assert SYMBOL_TO_OPERATION['+'] == 'add'
    assert SYMBOL_TO_OPERATION['-'] == 'subtract'
    assert SYMBOL_TO_OPERATION['*'] == 'multiply'
    assert SYMBOL_TO_OPERATION['/'] == 'divide'

# Tests for calculate_and_print & OperationCommand
@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("1", "2", "add", "The result of 1 add 2 is equal to 3"),
    ("3", "4", "subtract", "The result of 3 subtract 4 is equal to -1"),
    ("5", "6", "multiply", "The result of 5 multiply 6 is equal to 30"),
    ("8", "2", "divide", "The result of 8 divide 2 is equal to 4"),
    ("abc", "2", "add", "Invalid number input: abc or 2 is not a valid number."),  # Test invalid input
    ("1", "2", "power", "Unknown operation: power"),  # Test unknown operation
    ("1", "0", "divide", "An error occurred: Cannot divide by zero."),  # Test division by zero
    ("5", "3", "add", "The result of 5 add 3 is equal to 8"),
    ("10", "2", "subtract", "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", "multiply", "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", "divide", "The result of 20 divide 4 is equal to 5"),
    ("1", "0", "divide", "An error occurred: Cannot divide by zero."),  # Adjusted for the actual error message
    ("9", "3", "unknown", "Unknown operation: unknown"),  # Test for unknown operation
    ("a", "3", "add", "Invalid number input: a or 3 is not a valid number."),  # Testing invalid number input
    ("5", "b", "subtract", "Invalid number input: 5 or b is not a valid number.")  # Testing another invalid number input
])

def test_calculate_and_print(a_string, b_string, operation_string, expected_string, capsys):
    '''Test user input as strings'''
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == expected_string

# Testing main() function
def test_main_invalid_arguments(capsys):
    '''Test main function with invalid number of command-line arguments'''
    with pytest.raises(SystemExit):
        main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Usage: python calculator_main.py <number1> <number2> <operation>"

def test_main_correct_arguments(capsys):
    '''Test providing the correct number of command-line arguments.'''
    test_input = ["calculator_main.py", "5", "3", "+"]
    expected_output = "The result of 5 add 3 is equal to 8\n"
    sys.argv = test_input
    main()
    captured = capsys.readouterr()
    assert captured.out == expected_output
