def min_sum(arr):
    summa = 0
    arr.sort()
    for i in range(len(arr) // 2):
        summa += arr[i] * arr[-i - 1]
    
    return summa
