def solve(a):
    return (lambda i: 'R' * ((a[-1] > a[0]) - (a[-1] < a[0]) == i) + 'UDA'[i])(__import__('collections').Counter(((x > y) - (x < y) for (x, y) in zip(a[-1:] + a, a))).most_common(1)[0][0])
