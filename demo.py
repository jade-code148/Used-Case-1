# math_operations.py

def add(a: int, b: int) -> int:
    """
    Adds two integers and returns the result.
    """
    return a + b

def subtract(a: int, b: int) -> int:
    """
    Subtracts the second integer from the first and returns the result.
    """
    return a - b

def multiply(a: int, b: int) -> int:
    """
    Multiplies two integers and returns the result.
    """
    return a * b

def divide(a: int, b: int) -> float:
    """
    Divides the first integer by the second and returns the result.
    Raises ValueError if the second integer is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
