from math import factorial as f


def ssc_forperm(arr):
    return (lambda fac: [{'total perm': fac}, {'total ssc': fac * (len(arr) + 1) / 2 * sum(arr)}, {'max ssc': sum([(i + 1) * a for (i, a) in enumerate(sorted(arr))])}, {'min ssc': sum([(i + 1) * a for (i, a) in enumerate(sorted(arr, reverse=True))])}])(f(len(arr)) / reduce(lambda a, b: a * b, [arr.count(x) for x in set(arr)]))
