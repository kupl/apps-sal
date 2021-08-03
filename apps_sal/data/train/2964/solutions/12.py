def sum_two_smallest_numbers(numbers):
    lowest_num1 = numbers[0]
    index = 0
    for i in range(0, len(numbers)):
        if lowest_num1 > numbers[i]:
            lowest_num1 = numbers[i]
            index = i
    numbers.pop(index)
    lowest_num2 = numbers[0]
    for i in range(0, len(numbers)):
        if lowest_num2 > numbers[i]:
            lowest_num2 = numbers[i]
            index = i
    return lowest_num1 + lowest_num2
