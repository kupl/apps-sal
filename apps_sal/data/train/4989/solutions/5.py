def hollow_triangle(n):
    if n == 1:
        return ['
    first = ["_" * (n - 1) + "
    last = ["
    return first + ["_" * (n - i - 1) + "
