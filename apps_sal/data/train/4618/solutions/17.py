def positive_sum(arr):
    summ = 0
    for num in arr:
        if num >= 0:
            summ += num
    return summ
