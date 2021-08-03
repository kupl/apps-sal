def is_dd(n):
    for i in set([int(d) for d in str(n)]):
        if str(n).count(str(i)) == i:
            return True
    return False
