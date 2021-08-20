def sum_str(a, b):
    return str(int(a) + int(b)) if a.isnumeric() and b.isnumeric() else a if not b.isnumeric() and a.isnumeric() else b if not a.isnumeric() and b.isnumeric() else '0' if not a.isnumeric() and (not b.isnumeric()) else 0
