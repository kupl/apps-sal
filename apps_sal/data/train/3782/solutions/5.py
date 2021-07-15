def check_three_and_two(array):
    return len(set(array)) == 2 and array.count(array[0]) not in [1,4]
