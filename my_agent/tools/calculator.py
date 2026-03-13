import math

def calculator(operation: str, a: float, b: float) -> str:
    """
    Use this tool only for arithmetic and numeric calculations.

    Supported operations:
    - add
    - subtract
    - multiply
    - divide
    - power
    - sqrt
    - modulo

    Args:
        operation: The arithmetic operation to perform.
        a: The first number.
        b: The second number. Use 0 if not needed.

    Returns:
        The numeric result as a string.

    Do not use this tool for language, translation, grammar, logic, reading, or file-analysis tasks.
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