def is_odd_heavy(arr):
    maxEven, minOdd = (f(filter(lambda n: n % 2 == v, arr), default=float("-inf")) for f, v in ((max, 0), (min, 1)))
    return maxEven < minOdd
