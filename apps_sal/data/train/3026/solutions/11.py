def min_value(digits):
    numbers = [False for x in range(10)]
    for x in digits:
        numbers[x] = True
    result = 0
    min = 1
    for i in range(9,0,-1):
        if numbers[i]:
            result += i*min
            min *= 10
    return result
