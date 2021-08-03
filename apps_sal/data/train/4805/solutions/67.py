def check(a, x):
    c = 0
    for i in range(len(a)):
        if(a[i] == x):
            c = 1
    if(c == 1):
        return True
    else:
        return False
