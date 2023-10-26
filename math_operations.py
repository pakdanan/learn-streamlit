# math_operations.py

def add(x, y):
    """
    Add two numbers.

    :param x: First number
    :param y: Second number
    :return: The sum of x and y

    >>> add(5, 3)
    8
    >>> add(-2, 7)
    5
    """
    return x + y


def subtract(x, y):
    """
    Subtract y from x.

    :param x: First number
    :param y: Second number
    :return: The result of x - y

    >>> subtract(10, 4)
    6
    >>> subtract(3, 7)
    -4
    """
    return x - y


def multiply(x, y):
    """
    Multiply two numbers.

    :param x: First number
    :param y: Second number
    :return: The product of x and y

    >>> multiply(5, 3)
    15
    >>> multiply(-2, 7)
    -14
    """
    return x * y


def divide(x, y):
    """
    Divide x by y.

    :param x: Numerator
    :param y: Denominator
    :return: The result of x / y

    >>> divide(10, 2)
    5.0
    >>> divide(8, 0)  # Division by zero
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    """
    if y == 0:
        raise ZeroDivisionError("division by zero")
    return x / y


if __name__ == "__main__":
    import doctest
    doctest.testmod()
