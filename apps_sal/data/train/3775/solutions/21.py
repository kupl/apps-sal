def digits(n):
#     return len(str(n))
    cont = 0
    while n > 9:
        n //= 10
        cont+=1
    return cont+1
