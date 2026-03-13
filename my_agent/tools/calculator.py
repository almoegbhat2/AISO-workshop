import math

def calculator(operation: str, a: float, b: float | None = None) -> str:
    """
    Perform numeric calculations.

    Use this tool whenever a question involves arithmetic or numeric computation.

    Supported operations:
    - add
    - subtract
    - multiply
    - divide
    - power
    - sqrt
    - modulo

    Args:
        operation: The calculation to perform.
        a: First number.
        b: Second number (not required for sqrt).

    Returns:
        The numeric result as a string.

    Raises:
        ValueError: If the operation is unsupported or invalid.
    """

    operation = operation.lower()

    if operation in ["add", "sum", "+"]:
        result = a + b

    elif operation in ["subtract", "minus", "-"]:
        result = a - b

    elif operation in ["multiply", "times", "*"]:
        result = a * b

    elif operation in ["divide", "/"]:
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        result = a / b

    elif operation in ["power", "exp", "^"]:
        result = a ** b

    elif operation in ["sqrt", "square_root"]:
        if a < 0:
            raise ValueError("Cannot take square root of negative number.")
        result = math.sqrt(a)

    elif operation in ["mod", "modulo", "%"]:
        result = a % b

    else:
        raise ValueError(f"Unsupported operation: {operation}")

    return str(result)