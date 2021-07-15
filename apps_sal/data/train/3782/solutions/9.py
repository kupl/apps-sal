def check_three_and_two(arr):
    for i in arr:
        if not 2 <=arr.count(i) <= 3:
            return False
    return True

