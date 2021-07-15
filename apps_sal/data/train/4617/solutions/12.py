def powers_of_two(n):
    pL = [1]
    for i in range(n):
        pL.append(pL[i]*2)
    return pL
