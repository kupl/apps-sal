def clonewars(k):
    return [2 ** max(0, k - 1), sum((2 ** max(0, i) * (k - i) for i in range(k)))]
