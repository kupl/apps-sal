def int_diff(a, n):
    return sum(abs(a[i] - a[j]) == n for i in range(len(a)) for j in range(i + 1, len(a)))
