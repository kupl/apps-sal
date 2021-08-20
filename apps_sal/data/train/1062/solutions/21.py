n = int(input())


def mini(a, b, n):
    if a < n and b < n:
        return min(a, b)
    elif a >= n and b < n:
        return min(2 * n - 2 - a, b)
    elif a < n and b >= n:
        return min(a, 2 * n - 2 - b)
    elif a >= n and b >= n:
        return min(2 * n - 2 - a, 2 * n - 2 - b)


for i in range(0, 2 * n - 1):
    for j in range(0, 2 * n - 1):
        temp = n - mini(i, j, n)
        print(temp, end=' ')
    print('')
