def sum_two_smallest_numbers(numbers):
    s = sorted(numbers)  # sorting numbers from lowest to highest
    return s[0] + s[1]  # returning the two smallest numbers on the list
