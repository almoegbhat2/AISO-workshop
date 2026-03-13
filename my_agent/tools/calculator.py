import math

def calculator(operation: str, a: float, b: float) -> str:
    """
    Perform numeric calculations.

    Supported operations:
    - add
    - subtract
    - multiply
    - divide
    - power (a raised to the power b)
    - sqrt (square root of a, ignore b)
    - modulo

    Use this tool whenever a question involves arithmetic or numeric computation.
    Always return the numeric result.
    """

    operation = operation.lower().strip()

    if operation in ["add", "+", "sum"]:
        result = a + b
    elif operation in ["subtract", "-", "minus"]:
        result = a - b
    elif operation in ["multiply", "*", "times"]:
        result = a * b
    elif operation in ["divide", "/", "division"]:
        result = a / b
    elif operation in ["power", "exp", "^", "exponent", "raised_to_power"]:
        result = a ** b
    elif operation in ["sqrt", "square_root"]:
        result = math.sqrt(a)
    elif operation in ["modulo", "mod", "%"]:
        result = a % b
    else:
        raise ValueError(f"Unsupported operation: {operation}")

    return str(result)