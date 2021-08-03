def positive_sum(arr):
    summ = 0
    for temp in arr:
        if temp > 0:
            summ += temp
    return summ
