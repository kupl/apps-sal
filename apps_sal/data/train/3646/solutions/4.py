subfactorial, factorial = [1, 0], [1]
for n in range(1, 10 ** 4):
    subfactorial.append(n * (subfactorial[-1] + subfactorial[-2]))
    factorial.append(n * factorial[-1])


def fixed_points_perms(n, k):
    return factorial[n] // factorial[n - k] // factorial[k] * subfactorial[n - k]
