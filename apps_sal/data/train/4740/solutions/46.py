def row_sum_odd_numbers(n):
    i = n
    numberx = 0
    while n > 0:
        numberx += n
        n -= 1
    v = numberx
    resultList = []
    result = 0
    for x in range(1, (numberx * 2) + 1):
        if x % 2 == 1:
            resultList.append(x)
    while v > (numberx - i):
        result += int(resultList[(v - 1)])
        v -= 1
    return result
