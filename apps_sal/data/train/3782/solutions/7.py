def check_three_and_two(array):
    ans = [array.count(i) for i in 'abc']
    return True if 2 in ans and 3 in ans else False

