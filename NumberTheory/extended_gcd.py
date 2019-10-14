# Extended Euclid's Algorithm : If d divides a and b and d = a*x + b*y for integers x and y, then d = gcd(a,b)


def extended_gcd(a, b):
    """
    >>> extended_gcd(10, 6)
    (2, -1, 2)

    >>> extended_gcd(7, 5)
    (1, -2, 3)

    """
    assert a >= 0 and b >= 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y

    return (d, x, y)



# Other form - When you want only output x and y not d = gcd(a,b)

# Extended Euclid
def extended_euclid(a, b):
    """
    >>> extended_euclid(10, 6)
    (-1, 2)

    >>> extended_euclid(7, 5)
    (-2, 3)

    """
    if b == 0:
        return (1, 0)
    (x, y) = extended_euclid(b, a % b)
    k = a // b
    return (y, x - k * y)


# import testmod for testing our function
from doctest import testmod

if __name__ == '__main__':
    testmod(name='extended_gcd', verbose=True)
    testmod(name='extended_euclid', verbose=True)
