def is_happy(n):
    seen = {n}
    while n != 1:
        n = sum(d*d for d in map(int, str(n)))
        if n in seen:
            return False
        seen.add(n)
    return True
