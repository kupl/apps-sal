def sum_two_smallest_numbers(numbers):
    # first we sort array in descending order and then take first two element
    # check "sorted()" in python
    return sorted(numbers)[0] + sorted(numbers)[1]
