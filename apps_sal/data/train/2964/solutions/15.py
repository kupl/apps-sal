def sum_two_smallest_numbers(numbers):
    tmp_numbers = numbers
    tmp_numbers.sort()

    return tmp_numbers[0] + tmp_numbers[1]
