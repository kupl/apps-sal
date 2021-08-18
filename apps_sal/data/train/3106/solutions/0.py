from math import factorial as fact


def combs_non_empty_boxes(n, k):
    if k < 0 or k > n:
        return 'It cannot be possible!'
    return sum([1, -1][i % 2] * (k - i)**n * fact(k) // (fact(k - i) * fact(i)) for i in range(k + 1)) // fact(k)
