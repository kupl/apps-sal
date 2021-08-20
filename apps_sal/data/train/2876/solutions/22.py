def check_helper(a, x, index):
    if index == len(a):
        return False
    if a[index] == x:
        return True
    return check_helper(a, x, index + 1)


def check(a, x):
    return check_helper(a, x, 0)
