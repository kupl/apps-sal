from bisect import bisect

def sum_of_threes(n, xs=[3**i for i in range(34)]):
    result = []
    while n >= 1:
        x = bisect(xs, n) - 1
        n -= 3 ** x
        result.append(x)
    return 'Impossible' if len(result) != len(set(result)) else '+'.join(f'3^{x}' for x in result)
