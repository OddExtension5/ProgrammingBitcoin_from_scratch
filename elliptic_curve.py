#  Elliptic curves are useful because of something called point addition.
#  Point addition is where we can do an operation on two of the points on the curve and get a third point, also on the curve.
#  It turns out that for every elliptic curve, a line will intersect it at either one point or three points, except in a couple of special cases it intersect at two points.
#  The two exceptions are when a line is exactly vertical and when a line is tangent to the curve.

#  The class represents a points in an Elliptic Curve

from fieldElement import FieldElement


class Point:

    def __init__(self, x, y, a, b):
        self.x, self.y, self.a, self.b = x, y, a, b

        if self.x is None and self.y is None:
            return

        if self.y ** 2 != self.x ** 3 + a * x + b:
            raise ValueError("({},{}) is not on the curve.".format(x, y))

    def __repr__(self):
        if self.x is None:
            return 'Point(infinity)'
        elif isinstance(self.x, FieldElement):
            return 'Point({},{})_{}_{} FieldElement({})'.format(self.x.num,
                                                                self.y.num, self.a.num, self.b.num, self.x.prime)
        else:
            return 'Point({],{})_{}_{}'.format(self.x, self.y, self.a, self.b)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.a == other.a and self.b == other.b

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError("Points ({},{}) are not on the curve.".format(self, other))

        if self.x is None:
            return other

        if other.x is None:
            return self

        if self.x == other.x and self.y != other.y:
            return type(self)(None, None, self.a, self.b)

        if self.x != other.x:
            s = (other.y - self.y) / (other.x - self.x)
            x = s ** 2 - self.x - other.x
            y = s * (self.x - x) - self.y

            return type(self)(x, y, self.a, self.b)

        if self == other:
            s = (3 * self.x ** 2 + self.a) / (2 * self.y)
            x = s ** 2 - 2 * self.x
            y = s * (self.x - x) - self.y

            return type(self)(x, y, self.a, self.y)

        if self == other and self.y == 0 * self.x:
            return type(self)(None, None, self.a, self.b)
