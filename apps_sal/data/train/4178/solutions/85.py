def min_sum(arr):
    a1 = sorted(arr,reverse = True)
    a2 = sorted(arr)
    return int(sum(x * y for x,y in zip(a1,a2)) / 2)
