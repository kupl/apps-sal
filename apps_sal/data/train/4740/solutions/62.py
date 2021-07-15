def row_sum_odd_numbers(n):
    num = 1
    for x in range(n):
        num = num + (2*x)
    #print(num)

    total = 0
    for x in range(n):
        total += num + (2*x)
    #print(total)
    return total
