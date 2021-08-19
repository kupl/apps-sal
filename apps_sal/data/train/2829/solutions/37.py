def array_madness(a, b):
    square = 0
    cube = 0
    for i in range(0, len(a)):
        square += a[i] ** 2
    for i in range(0, len(b)):
        cube += b[i] ** 3
    if square > cube:
        return True
    else:
        return False
