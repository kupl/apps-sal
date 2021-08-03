def johnann(n, jnota):
    j, a = [0], [1]
    for i in range(1, n):
        j.append(i - a[j[-1]])
        a.append(i - j[a[-1]])
    return j if jnota else a


def john(n): return johnann(n, True)
def ann(n): return johnann(n, False)
def sum_john(n): return sum(john(n))
def sum_ann(n): return sum(ann(n))
