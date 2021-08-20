import math


def count_paths(N, coords):
    (row, col) = coords
    if row == 0 and col == N - 1:
        return 0
    inverse_col = N - 1 - col
    return choose(row + inverse_col, inverse_col)


def choose(n, k):
    if k > n:
        return 0
    if k > n - k:
        k = n - k
    product = 1
    k_list = list(range(2, k + 1))
    for i in range(n, n - k, -1):
        if len(k_list) > 0:
            k_index = len(k_list) - 1
            k = k_list[k_index]
            if i % k == 0:
                i = i // k
                del k_list[k_index]
        product *= i
    for k in k_list:
        product //= k
    return product
