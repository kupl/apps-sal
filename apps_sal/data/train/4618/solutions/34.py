def positive_sum(arr):
    sum = 0
    for el in arr:
        if el > 0:
            sum += int(el)
    return sum
