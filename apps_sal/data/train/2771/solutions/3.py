def hofstadter_Q(n):
    a = [None, 1, 1]
    for i in range(3, n + 1):
        a.append(a[i - a[-1]] + a[i - a[-2]])
    return a.pop()
