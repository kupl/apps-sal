def array_madness(a, b):
    # Ready, get, set, GO!!!
    temp = 0
    temp1 = 0
    for i in range(len(a)):
        temp += a[i]**2
    for j in range(len(b)):
        temp1 += b[j]**3

    if temp > temp1:
        return True
    else:
        return False
