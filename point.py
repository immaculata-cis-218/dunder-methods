"""
Example Point Class which demonstrates use of dunder methods
Dr. Bill Wagner

Additional updates by Andrew Bowman
"""


class Point:
    """
    Defines a point on a chart
    """

    # pylint: disable=unidiomatic-typecheck,protected-access,invalid-name

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __repr__(self):
        """
        Return a complete representation of the object
        It is used for debugging and not designed for printing
        """
        return "Point(" + str(self.__x) + "," + str(self.__y) + ")"

    def __str__(self):
        """
        Returns a human readable string
        """
        return "(" + str(self.__x) + "," + str(self.__y) + ")"

    def __eq__(self, other):
        """
        Points are the same
        """
        if self is other:
            return True  # the two objects are really one
        if type(self) != type(other):
            return False  # The objects are not the same class so they can't be equal
        return self.__x == other.__x and self.__y == other.__y

    def __d(self):
        """
        This is a private function
        """
        return self.__x * self.__x + self.__y * self.__y

    # point comparisons look at distance from (0, 0)
    def __lt__(self, other):
        if type(self) != type(other):
            return False
        return self.__d() < other.__d()

    def __ge__(self, other):
        if type(self) != type(other):
            return False
        return self.__d() >= other.__d()


if __name__ == "__main__":
    p1 = Point(1, 1)
    print("Point 1 using repr():", repr(p1))
    print("Point 1 using print():", p1)

    p2 = Point(6, 7)
    print("Point 2 using repr():", repr(p2))
    print("Point 2 using print():", p2)

    p3 = p2
    print("Point 1 is Point 2:", p1 is p2)
    print("Point 3 is Point 2:", p3 is p2)
    print("Point 3 is equal to Point 2:", p3 == p2)
    print("Point 1 is less than Point 2:", p1 < p2)
    print("Point 1 is less than or equal to Point 2:", p1 <= p2)
    print("Point 1 is greater than Point 2:", p1 > p2)
    print("Point 1 is greater than or equal to Point 2:", p1 >= p2)
