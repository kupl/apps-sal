def sum_str(a, b):
    try:
        return str(int(a) + int(b))
    except ValueError:
        return '0' if a + b == '' else a + b
