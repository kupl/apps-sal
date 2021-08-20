def josephus_survivor(n, k):
    arr = [i for i in range(1, n + 1)]
    ptr = k - 1
    while len(arr) > 1:
        if ptr >= len(arr):
            ptr = ptr % len(arr)
        del arr[ptr]
        ptr += k - 1
    return arr[0]
