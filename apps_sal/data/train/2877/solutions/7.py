def count(a, t, x):
    return sum(1 for n in a if (n % x == t % x if x else n == t))
