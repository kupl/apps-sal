def powers(n):
    return [1<<i for i, x in enumerate(reversed(bin(n))) if x == "1"]
