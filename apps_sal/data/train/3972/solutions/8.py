def find_next_square(sq):
    import math
    f = float(sq)
    root = math.sqrt(f)
    if root.is_integer():
        next_int = int(root) + 1
        next_square = next_int * next_int
        return next_square
    else:
        return -1

