k, li = 1, [0]

for i in range(1, 1000000):
    li.append(k)
    k += 8 * i


def branch(n):
    a, b = next([i, li[i - 1] + 1] for i, j in enumerate(li) if j >= n)
    step = a * 2 - 2
    for i in range(4):
        if b <= n < b + step:
            return i
        b += step
    return 0
