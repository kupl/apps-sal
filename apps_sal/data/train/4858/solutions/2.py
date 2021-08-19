def get_arrays(n, name):
    a = [1]
    j = [0]
    for i in xrange(1, n):
        next_j = i - a[j[i - 1]]
        j.append(next_j)
        next_a = i - j[a[i - 1]]
        a.append(next_a)
    ret = {'john': j, 'ann': a}
    return ret[name]


def john(n):
    return get_arrays(n, 'john')


def ann(n):
    return get_arrays(n, 'ann')


def sum_john(n):
    return sum(john(n))


def sum_ann(n):
    return sum(ann(n))
