def row_sum_odd_numbers(n):
    startPoint = 1
    counter = 1
    mainNumber = 1
    sum = 0
    for num in range(n - 1, 0, -1):
        startPoint += num
    while counter < startPoint:
        if counter == startPoint:
            break
        else:
            mainNumber += 2
            counter += 1
    for i in range(mainNumber, mainNumber + n * 2, 2):
        sum += i
    return sum
