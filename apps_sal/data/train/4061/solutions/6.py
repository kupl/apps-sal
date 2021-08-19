from math import gcd
seq = [7]
diff = [1]
for i in range(2, 100001):
    seq.append(seq[-1] + gcd(i, seq[-1]))
    diff.append(seq[-1] - seq[-2])
unique = [5, 3, 11, 23, 47, 101, 7, 13, 233, 467, 941, 1889, 3779, 7559, 15131, 53, 30323, 60647, 121403, 242807, 19, 37, 17, 199, 29, 486041, 421, 972533, 577]


def count_ones(n):
    return diff[:n].count(1)


def max_pn(n):
    return max(unique[:n])


def an_over_average(n):
    return 3 * n / n
