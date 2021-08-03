def finding_k(arr):
    for n in range(max(arr) - 1, 0, -1):
        if len({x % n for x in arr}) == 1:
            return n
    return -1
