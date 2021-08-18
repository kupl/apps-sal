from math import factorial as fact
A000166 = [1, 0]
for n in range(2, 9000):
    A000166.append((n - 1) * (A000166[n - 1] + A000166[n - 2]))


def fixed_points_perms(n, k):
    if n < k:
        return 0
    return A000166[n - k] * fact(n) // (fact(k) * fact(n - k))
