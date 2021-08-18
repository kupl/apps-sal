n = int(input())


if n % 4 > 1:

    print(-1)

    return


a = [i for i in range(0, n + 1)]

for i in range(1, n // 2 + 1, 2):

    p, q, r, s = i, i + 1, n - i, n - i + 1

    a[p], a[q], a[r], a[s] = a[q], a[s], a[p], a[r]


def check(arr):

    for i in range(1, n + 1):

        k = arr[i]

        if arr[arr[k]] != n - k + 1:

            return False

    return True


# print(check(a))
print(*a[1:])
