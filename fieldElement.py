class FieldElement:

    def __init__(self, num, prime):
        if num < 0 and num >= prime:
            raise ValueError("Number {} not in field range 0 to {}.".format(num, prime - 1))

        self.num = num
        self.prime = prime

    def __repr__(self):
        return "FieldElement_{}({})".format(self.prime, self.num)

    def __eq__(self, other):
        if other is None:
            return False

        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        if other is None:
            return False

        return not (self == other)

    def __add__(self, other):

        if self.prime != other.prime:
            raise TypeError("Cannot add two numbers in different fields")

        num = (self.num + other.num) % self.prime

        return type(self)(num, self.prime)

    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError("Cannot subtract two numbers in different fields")

        num = (self.num - other.num) % self.prime

        return type(self)(num, self.prime)

    def __mul__(self, other):

        if self.prime != other.prime:
            raise TypeError("Cannot multiply two numbers in different fields")

        num = (self.num * other.num) % self.prime

        return type(self)(num, self.prime)

    def __pow__(self, exponent):
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)

        return type(self)(num, self.prime)

    def __truediv__(self, other):

        if self.prime != other.prime:
            raise ValueError("Cannot divide two numbers in different fields.")

        num = (self.num * pow(other.num, self.prime - 2, self.prime)) % self.prime

        return type(self)(num, self.prime)

    def __rmul__(self, coefficient):
        num = (self.num * coefficient) % self.prime

        return type(self)(num, self.prime)
