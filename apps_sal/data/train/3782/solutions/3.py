def check_three_and_two(array):
    return {array.count(i) for i in array} == {2, 3}
