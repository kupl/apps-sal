def factors(n):
    seen = {1, n}
    for a in range(2, 1 + int(n ** 0.5)):
        b, m = divmod(n, a)
        if m == 0:
            if a in seen: break
            seen.add(a)
            seen.add(b)
    return sorted(seen)

def consecutive_sum(num):
    return sum(1 for d in factors(num) if d % 2)
