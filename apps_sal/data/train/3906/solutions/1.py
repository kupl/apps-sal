def total(arr):
    from math import factorial as fact

    def choose(a, b):
        return fact(a) / (fact(a - b) * fact(b))
    return sum((choose(len(arr) - 1, i) * v for (i, v) in enumerate(arr)))
