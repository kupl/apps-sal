from functools import reduce


def find_min_max_product(arr, k):
    if k <= len(arr):
        arr = sorted(arr, key=abs)
        lasts = arr[-k:]
        v1 = reduce(int.__mul__, lasts)
        v0 = reduce(int.__mul__, arr[:k])
        first_SameOrOpp = [next((v for v in lasts if cmp(v < 0, v1 < 0)), None) for cmp in (int.__eq__, int.__ne__)]
        prevVal_OppOrSame = [next((v for v in reversed(arr[:-k]) if cmp(v < 0, v1 < 0)), None) for cmp in (int.__ne__, int.__eq__)]
        ans = [v0, v1] + [v1 * n // f for (f, n) in zip(first_SameOrOpp, prevVal_OppOrSame) if None not in (f, n)]
        return (min(ans), max(ans))
