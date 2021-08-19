def power_sumDigTerm(n):
    # your code here
    return sorted([a**b for a in range(2, 100) for b in range(2, 100) if a == sum(map(int, str(a**b)))])[n - 1]
