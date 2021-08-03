def array_madness(a, b):
    count = 0
    for item in a:
        a[count] = item**2
        count += 1
    count = 0
    for item in b:
        b[count] = item**3
        count += 1

    if sum(a) > sum(b):
        return True
    else:
        return False
