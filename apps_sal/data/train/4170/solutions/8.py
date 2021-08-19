def super_sum(D, N):
    summe = 0
    for i in range(0, N):
        summe += i
    erg = summe * D * N ** (D - 1)
    return erg
