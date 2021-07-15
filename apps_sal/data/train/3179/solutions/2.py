def min_and_max(l, d, x):
    return [next(i for i in range(l, d+1) if sum(int(n) for n in str(i)) == x),
            next(i for i in range(d, l-1, -1) if sum(int(n) for n in str(i)) == x)]
