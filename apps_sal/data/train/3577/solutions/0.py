from collections import Counter

def fib_digits(n):
    a, b = 0, 1
    for i in range(n): a, b = b, a+b
    return sorted(((b, int(a)) for a, b in Counter(str(a)).items()), reverse=True)
