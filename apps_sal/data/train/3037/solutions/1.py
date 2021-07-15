from bisect import insort

def obtain_max_number(arr):
    arr = sorted(arr)
    while True:
        prev = -1
        for i, x in enumerate(arr):
            if x == prev:
                break
            prev = x
        else:
            return max(arr)
        insort(arr, arr.pop(i) + arr.pop(i-1))
