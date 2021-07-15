def compute_depth(n):
    seen = set()
    for i in range(1, 99999999):
        seen.update(str(n * i))
        if len(seen) == 10:
            return i
