summ = list()


def partition(n, k):
    if n >= 0 and k >= 0 and summ[n][k] > 0:
        return summ[n][k]
    if n < 0:
        return 0
    if n <= 1 or k == 1:
        return 1
    summ[n][k] = partition(n, k - 1) + partition(n - k, k)
    return summ[n][k]


def partitions(n):
    n += 1
    for i in range(n):
        summ.append(list())
        for j in range(n):
            summ[i].append(-1)
    return partition(n - 1, n - 1)
