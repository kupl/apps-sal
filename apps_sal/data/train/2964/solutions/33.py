def sum_two_smallest_numbers(numbers):
    result = 0
    for i in range(2):
        min = numbers[0]
        for num in numbers:
            if num < min:
                min = num
        numbers[numbers.index(min)] = max(numbers) + 1
        result += min
    return result
