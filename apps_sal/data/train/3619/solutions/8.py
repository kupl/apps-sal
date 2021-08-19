def is_dd(n):
    return any((int(c) == x for (c, x) in __import__('collections').Counter(str(n)).items()))
