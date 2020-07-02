
# Changing the String Representation of Instances
# using __str()__  and __repr__()


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Pair({self.x},{self.y})"

    def __str__(self):
        return f"({self.x},{self.y})"


p = Pair(3, 4)
print(f"p is {p!r}")
# !r - tells the interpreter to use __repr__()

print(f"p is {p}")
# This uses __str__() function by default

