# lcm(a,b) of integers a & b ( both different from zero) is the smallest positive integer that is divisible by both a and b

# we know lcm(a,b) * gcd(a,b) = a*b

# Importing gcd from euclid's algorithm.py

from euclids_algorithm import gcd


def lcm(a, b):
    assert a > 0 and b > 0

    return (a * b) / gcd(a, b)
