def hofstadter_Q(n):
    a = [1, 1]
    for i in range(2, n):
        a.append(a[i - a[i - 1]] + a[i - a[i - 2]])
    return a[n - 1]
