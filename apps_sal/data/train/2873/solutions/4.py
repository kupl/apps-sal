def josephus_survivor(n,k):
    arr = [i + 1 for i in range(n)]
    if len(arr) == 1:
        return arr[0]
    cur_pos = k - 1
    while len(arr) != 1:
        while cur_pos >= len(arr):
            cur_pos = cur_pos - len(arr)
        arr.pop(cur_pos)
        cur_pos += k - 1
    return arr[0]
