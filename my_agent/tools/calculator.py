import math

def calculator(operation: str, a: float, b: float) -> str:
    """
    Perform arithmetic calculations.

    Args:
        operation: add, subtract, multiply, divide, power, sqrt, modulo
        a: first number
        b: second number (use 0 if not needed)

    Returns:
        The numeric result.
    """

    operation = operation.lower()

    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        result = a / b
    elif operation == "power":
        result = a ** b
    elif operation == "sqrt":
        result = math.sqrt(a)
    elif operation == "modulo":
        result = a % b
    else:
        raise ValueError("Unsupported operation")

    return str(result)