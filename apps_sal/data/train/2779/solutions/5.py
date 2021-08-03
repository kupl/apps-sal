def fib_rabbits(n, b):
    obj = {'IP': 1, 'AP': 0}
    for month in range(1, n + 1):
        cur = obj['IP']
        obj['IP'] = b * obj['AP']
        obj['AP'] += cur

    return obj['AP']
