from collections import Counter


def fib_digits(n):
    a,b = 0,1
    for i in range(n-1):
        a,b = b, a+b
    counts = Counter(str(b))
    return sorted(((count, int(digit)) for digit, count in counts.items()), reverse=True)
