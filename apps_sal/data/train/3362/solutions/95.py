def sum_mix(arr):
    sum = 0
    for i in arr:
        if type(i) == str:
            i = int(i)
            sum += i
        else:
            sum += i
    return sum
