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



# Recursive Euclid's Algorithm

def recursive_greatest_common_divisor(a, b):
    """
    >>> recursive_greatest_common_divisor(7,5)
    1

    Note : In number theory, two integers a and b are said to be relatively prime, mutually prime, or co-prime
           if the only positive integer (factor) that divides both of them is 1  i.e., gcd(a,b) = 1.

    >>> recursive_greatest_common_divisor(121, 11)
    11

    """

    if b == 0:
        return a
    return recursive_greatest_common_divisor(b, a % b)



# import testmod for testing our function
from doctest import testmod

if __name__ == '__main__':
    testmod(name='recursive_greatest_common_divisor', verbose=True)
    testmod(name='greatest_common_divisor', verbose=True)
