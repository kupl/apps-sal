def sum_of_minimums(numbers):
    sum_num = 0
    for item in range(len(numbers)):
        sum_num += min(numbers[item])
    return sum_num
