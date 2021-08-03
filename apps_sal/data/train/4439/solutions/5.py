def divisors(n):
    ans = set()
    for i in range(1, int(n**.5) + 1):
        if not n % i:
            ans |= {i, n // i}
    return len(ans)


def div_num(a, b):
    if a > b:
        return "Error"
    return sorted(((n, divisors(n)) for n in range(a, b + 1)), key=lambda x: x[1], reverse=1)[0][0]
