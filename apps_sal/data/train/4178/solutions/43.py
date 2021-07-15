def min_sum(arr):
    lst = []
    
    arr = sorted(arr)
    
    for i in range(len(arr) // 2):
        lst.append(arr[-i-1] * arr[i])
    return sum(lst)

