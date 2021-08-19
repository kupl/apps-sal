def check_three_and_two(array):
    return True if len(set(array)) == 2 and [each for each in set(array) if array.count(each) in [2, 3]] else False
