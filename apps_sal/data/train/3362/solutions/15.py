def sum_mix(arr):
    sum = 0
    for i in arr:
        if type(i) != int:
            sum += int(i)
        else:
            sum += i
    return sum
