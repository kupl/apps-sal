def sum_dig_pow(a, b):
    ans = []
    while a <= b:
        if sum((int(j) ** k for (j, k) in zip(str(a), range(1, len(str(a)) + 1)))) == a:
            ans += [a]
        a += 1
    return ans
