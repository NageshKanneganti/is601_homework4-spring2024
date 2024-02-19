'''main.py: Capture user input and handle invalid input/exceptions'''
import sys # for command-line arguments
from decimal import Decimal, InvalidOperation # for handeling invalid inputs
from calculator import Calculator

# Define a mapping of symbols to operation names
SYMBOL_TO_OPERATION = {
    '+': 'add',
    '-': 'subtract',
    '*': 'multiply',
    '/': 'divide'
}

class OperationCommand:
    '''Executes a specific arithmetic operation'''

    def __init__(self, calculator, operation_name, a, b):
        '''Initialize OperationCommand instances'''
        self.calculator = calculator
        self.operation_name = operation_name
        self.a = a
        self.b = b

    def execute(self):
        '''Validiate operation'''
        # Retrieve the operation method from the Calculator class using getattr
        operation_method = getattr(self.calculator, self.operation_name, None)
        if operation_method:
            try:
                return operation_method(self.a, self.b)
            except:
                raise ZeroDivisionError("Cannot divide by zero.")
        else:
            raise ValueError(f"Unknown operation: {self.operation_name}")
    
def calculate_and_print(a, b, operation_name):
    '''If valid input performs operation using OperationCommand instance; Handles exceptions (invalid input, unknown operations, and other generic exceptions)'''
    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        command = OperationCommand(Calculator, operation_name, a_decimal, b_decimal)
        result = command.execute()
        print(f"The result of {a} {operation_name} {b} is equal to {result}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    '''Checks if correct number of command-line arguments is provided'''
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)
    
    _, a, b, operation_name = sys.argv

    # Check if the provided operation is a symbol and map it to the corresponding operation name
    operation_name = SYMBOL_TO_OPERATION.get(operation_name, operation_name)

    calculate_and_print(a, b, operation_name)
