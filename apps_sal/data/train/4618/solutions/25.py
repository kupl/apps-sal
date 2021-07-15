def positive_sum(arr):
    sum = 0
    if arr:
        for numb in arr:
            if (numb > 0):
                sum = sum + numb
    return sum

