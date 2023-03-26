class Point(object):
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
        """Points are the same"""
        if self is other:
            return True  # the two objects are really one
        elif type(self) != type(other):
            return False  # The objects are not the same class so they can't be equal
        else:
            return self.__x == other.__x and self.__y == other.__y

    def __d(self):
        """This is a privite function"""
        return self.__x * self.__x + self.__y * self.__y

    # point comparisions look at distance from (0, 0)
    def __lt__(self, other):
        if type(self) != type(other):
            return False
        return self.__d() < other.__d()

    def __ge__(self, other):
        if type(self) != type(other):
            return False
        return self.__d() >= other.__d()
