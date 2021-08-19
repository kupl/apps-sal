def odd_one_out(s):
    return [c for (c, n) in __import__('collections').Counter(s[::-1]).items() if n & 1][::-1]
