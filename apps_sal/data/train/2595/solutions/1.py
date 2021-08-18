
import cmath


def __starting_point():
    cnum = complex(input().strip())

    print(abs(cnum))
    print(cmath.phase(cnum))


__starting_point()
