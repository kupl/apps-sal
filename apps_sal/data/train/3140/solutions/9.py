def happy_numbers(n):
    return [k for k in range(1, n + 1) if is_happy(k)]


def is_happy(n):
    seen = {n}
    while n != 1:
        n = sum((int(d) ** 2 for d in str(n)))
        if n in seen:
            return False
        seen.add(n)
    return True
