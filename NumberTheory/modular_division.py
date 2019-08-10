# Modular Division
# Implement an efficient algorithm for dividing b by a modulo n.

# Given three integers a, b, and n, such that gcd(a,n)=1 and n>1, the algorithm should return an integer x such that
#        0≤x≤n−1, and  b/a=x(modn) (that is, b=ax(modn)).

# Theorem:
# a has a multiplicative inverse modulo n iff gcd(a,n) = 1


# This find x = b*a^(-1) mod n
# Uses ExtendedEuclid to find the inverse of a
from extended_gcd import extended_gcd, ExtendedEuclid


def modular_division(a, b, n):
    assert n > 1 and a > 0 and gcd(a, n) == 1
    (d, t, s) = extended_gcd(n, a)
    x = (b * s) % n
    return x


# This function find the inverses of a i.e., a^(-1)
def InvertModulo(a, n):
    (b, x) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b


# This function used the above inversion of a to find x = (b*a^(-1))mod n
def modular_division2(a, b, n):
    s = InvertModulo(a, n)
    x = (b * s) % n
    return x
