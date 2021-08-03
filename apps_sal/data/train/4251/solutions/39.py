def difference_of_squares(n):
    output = 0
    output2 = 0
    for i in range(0, n + 1):
        output += i
        output2 += i ** 2
    return output ** 2 - output2
