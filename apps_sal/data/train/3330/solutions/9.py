def make_triangle(m,n):
    if n == m:
        return m

    else:
        Num = len(range(m,n+1))

        elNum = 0
        k = 1
        while elNum < Num:
            k += 1
            elNum = int(k*(k+1)/2)
        
        if elNum != Num:
            return ""
    
    Lyr = (k-1)//3 + 1


    L1 = []
    for i in range(k):
        L1.append([])
        for j in range(k+i):
            L1[-1].append(" ")
        L1[-1].append("\n")

    el = m-1

    for CLyr in range(Lyr):
        topR = 2*CLyr
        topC = -2*(CLyr+1)
        
        CSize = k - 3*CLyr

        for i in range(CSize):
            el += 1
            L1[topR+i][-2*(1+CLyr)] = str(el % 10)

        for i in range(CSize-1):
            el += 1
            L1[topR+CSize-1][-4-2*(i+CLyr)] = str(el % 10)

        for i in range(CSize-2):
            el += 1
            L1[topR+CSize-1-1-i][i+1+CLyr*3] = str(el % 10)

    L2 = [e for inner_list in L1 for e in inner_list][:-1]
    return "".join(L2)
