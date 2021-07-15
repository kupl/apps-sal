def hotpo(n):
    res = n
    cont =0
    while res != 1:
        res = res/2 if res%2==0 else res*3 + 1
        cont +=1
    return cont
