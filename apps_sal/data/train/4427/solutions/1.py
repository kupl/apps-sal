def sum_groups(arr):
    lenArr, arr = -1, arr[:]
    while lenArr != len(arr):
        parity, lenArr, next = -1, len(arr), []
        while arr:
            val = arr.pop()
            if parity != val%2:
                next.append(val)
                parity = val%2
            else:
                next[-1] += val
        arr = next
    return len(arr)
