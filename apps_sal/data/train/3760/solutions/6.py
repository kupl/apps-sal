def roundRobin(a, n, i):
    return sum((min((a[i] + n * (i >= j) - 1) // n * n, v) for (j, v) in enumerate(a)))
