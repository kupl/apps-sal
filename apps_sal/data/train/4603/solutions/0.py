from numbers import Number


def Ackermann(m, n):
    if isinstance(n, Number) and isinstance(m, Number):
        if m >= 0 and n >= 0:
            return Ackermann_Aux(m, n)

    return None


def Ackermann_Aux(m, n):

    if m == 0:
        return n + 1

    if m > 0:
        if n == 0:
            return Ackermann_Aux(m - 1, 1)

        if n > 0:
            return Ackermann_Aux(m - 1, Ackermann_Aux(m, n - 1))
