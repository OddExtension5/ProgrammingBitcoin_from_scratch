#lcm(a,b) of integers a & b ( both different from zero) is the smallest positive integer that is divisible by both a&b

# we know lcm(a,b) * gcd(a,b) = a*b


def lowest_common_multiple(a, b):
    """
    >>> lowest_common_multiple(3,2)
    6

    >>> lowest_common_multiple(12, 80)
    240

    Note: The Least Common Multiple (LCM), lowest common multiple, or smallest common multiple of two integers a and b,
          usually denoted by LCM(a, b), is the smallest positive integer that is divisible by both a and b.
    """
    assert a > 0 and b > 0

    return (a * b) / greatest_common_divisor(a, b)


# Euclid's Lemma :  d divides a and b, if and only if d divides a-b and b

# Euclid's Algorithm

def greatest_common_divisor(a, b):
    """
    >>> greatest_common_divisor(7,5)
    1

    Note : In number theory, two integers a and b are said to be relatively prime, mutually prime, or co-prime
           if the only positive integer (factor) that divides both of them is 1  i.e., gcd(a,b) = 1.

    >>> greatest_common_divisor(121, 11)
    11

    """
    if a < b:
        a, b = b, a

    while a % b != 0:
        a, b = b, a % b

    return b


# import testmod for testing our function
from doctest import testmod

if __name__ == '__main__':
    testmod(name='lcm', verbose=True)
    testmod(name='greatest_common_divisor', verbose=True)
