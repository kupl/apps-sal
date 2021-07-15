def compute_depth(n):
    i = 0
    digits = set()
    while len(digits) < 10:
        i += 1
        digits.update(str(n * i))
    return i
