def sum_two_smallest_numbers(numbers):
    temp_list = numbers
    temp_list.sort()
    return temp_list[0] + temp_list[1]
