def check_three_and_two(array):
    return {array.count(x) for x in set(array)} == {2, 3}
