def check_three_and_two(array):
    return max([array.count(a) for a in array]) == 3 and min([array.count(a) for a in array]) == 2
