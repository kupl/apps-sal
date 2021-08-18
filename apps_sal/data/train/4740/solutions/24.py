def row_sum_odd_numbers(row):
    total = 0
    for i in range(1, row + 1):
        total += 1 * i

    sum = 0
    lastInt = total * 2 - 1
    startInt = lastInt - ((row - 1) * 2) - 1
    for i in range(lastInt, startInt, -2):
        sum += i

    return sum
