def calculator(operation: str, a: float, b: float) -> str:
    """
    Perform basic arithmetic operations.

    Args:
        operation: The operation to perform. Supported values: "add", "subtract", "multiply", "divide".
        a: The first number.
        b: The second number.

    Returns:
        The result of the calculation as a string.

    Raises:
        ValueError: If an unsupported operation is provided or division by zero occurs.
    """

    if operation == "add":
        result = a + b
    elif operation == "subtract":
        result = a - b
    elif operation == "multiply":
        result = a * b
    elif operation == "divide":
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        result = a / b
    else:
        raise ValueError(f"Unsupported operation: {operation}")

    return str(result)