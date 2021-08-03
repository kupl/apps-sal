def is_dd(n):
    for i in range(1, 10):
        if str(n).count(str(i)) == i:
            return True
    return False
