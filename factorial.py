def factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer using recursion.
    
    Args:
        n (int): Non-negative integer to compute factorial for.
        
    Returns:
        int: The factorial of n.
        
    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("Factorial is only defined for integers.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1
        
    return n * factorial(n - 1)


if __name__ == "__main__":
    # Test cases
    test_values = [0, 1, 5, 10]
    
    print("--- Factorial Calculation ---")
    for val in test_values:
        print(f"{val}! = {factorial(val)}")