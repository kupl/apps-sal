def sum_of_minimums(numbers):
    sum = 0
    for i in range(len(numbers)):
        min = numbers[i][0]
        for j in range(1, len(numbers[i])):
            if numbers[i][j] < min:
                min = numbers[i][j]
        sum += min
    return sum
