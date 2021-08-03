def check(a, x, i=0):
    if x == a[i]:
        return True
    if i == len(a) - 1:
        return False
    else:
        return check(a, x, i=i + 1)
