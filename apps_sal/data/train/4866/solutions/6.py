from itertools import chain

def f1(n):
    x = n // 2
    if x % 2:
        return x, n-x
    else:
        return x-1, x+1

def f3(n):
    m = n
    while m % 2 == 0:
        m //= 2
    return [m] * (n // m)

fs = [f1, lambda n: [1, n-1], f3, lambda n: [1] * n]

def split_all_even_numbers(numbers, way):
    return list(chain.from_iterable([n] if n % 2 else fs[way](n) for n in numbers))
