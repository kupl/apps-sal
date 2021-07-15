def find_2nd_largest(arr):
    from collections import defaultdict
    d = defaultdict(list)
    for elem in arr:
        d[type(elem)].append(elem)
    numbers = d[int]
    largest_num = 0
    second_largest_num = 0
    for number in numbers:
        if largest_num < number:
            largest_num = number
    for number in numbers:
        if second_largest_num < number and number < largest_num:
            second_largest_num = number
    if second_largest_num == 0:
        return None
    else:
        return second_largest_num
