def multiples(m, n):
    myarr = []
    for i in range(1, m + 1):
        myarr.append(n * i)
        i += 1
    return myarr
