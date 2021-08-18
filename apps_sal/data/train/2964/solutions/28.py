def sum_two_smallest_numbers(numbers):
    sorted_list = sorted(numbers)
    sum_of_smallest_number = sorted_list[0] + sorted_list[1]
    return sum_of_smallest_number
