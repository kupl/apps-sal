def power_of_two(n):
    if n == 0:
        return False
    if n & n - 1:
        return False
    else:
        return True
