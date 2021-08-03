def finding_k(arr):
    for i in range(max(arr) - 1, 0, -1):
        if len({j % i for j in arr}) == 1:
            return i
    return -1
