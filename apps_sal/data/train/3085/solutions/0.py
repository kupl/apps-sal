def aks_test(p):
    lst = []
    for i in range(2, p+1):
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    if p in lst:
        return True
    else:
        return False
