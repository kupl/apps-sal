def my_add(a, b):
    return a + b if isinstance(a, (int, float, complex)) and isinstance(b, (int, float, complex)) else None
