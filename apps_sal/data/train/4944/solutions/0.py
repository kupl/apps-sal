import math


class VectorInputCoordsValidationError(Exception):
    """Custom exception class for invalid input args given to the Vector instantiation"""


class Vector:
    # https://www.mathsisfun.com/algebra/vectors.html

    def __init__(self, *args):
        try:
            self.x, self.y, self.z = args if len(args) == 3 else args[0]
        except ValueError:
            raise VectorInputCoordsValidationError('Either give single iterable of 3 coords or pass them as *args')

    def __add__(self, other) -> "Vector":
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __sub__(self, other) -> "Vector":

        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def __eq__(self, other) -> bool:
        # https://www.grc.nasa.gov/www/k-12/airplane/vectcomp.html
        # https://onlinemschool.com/math/library/vector/equality/
        return all((
            self.x == other.x,
            self.y == other.y,
            self.z == other.z
        ))

    def cross(self, other) -> "Vector":
        # https://www.mathsisfun.com/algebra/vectors-cross-product.html
        return Vector(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def dot(self, other) -> int:
        # https://www.mathsisfun.com/algebra/vectors-dot-product.html
        return self.x * other.x + self.y * other.y + self.z * other.z

    def to_tuple(self) -> tuple:
        return self.x, self.y, self.z

    def __str__(self) -> str:
        return "<{x}, {y}, {z}>".format(**self.__dict__)

    @property
    def magnitude(self) -> float:
        return math.sqrt(
            sum(
                (
                    self.x ** 2,
                    self.y ** 2,
                    self.z ** 2
                )
            )
        )
