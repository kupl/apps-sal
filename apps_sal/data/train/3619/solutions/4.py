def is_dd(n):
    n = str(n)
    for i in range(1, 10):
        if n.count(str(i)) == i:
            return True
    return False
