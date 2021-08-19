def sort_twisted37(a):
    return sorted(a, key=lambda n: int(str(n).translate(str.maketrans('37', '73'))))
