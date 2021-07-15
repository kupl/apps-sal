def solution(a):
    elem = min(a)
    m = elem
    for i in range(len(a)):
        if (a[i] % elem != 0):
            elem = a[i] % elem
            if (m % elem != 0):
                elem = m % elem
    return abs(elem*len(a))

