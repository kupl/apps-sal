from itertools import zip_longest as z
def compare(s1, s2): return next(([1, -1][int(i) < int(j)] for i, j in z(s1.split('.'), s2.split('.'), fillvalue='0') if int(i) != int(j)), 0)
