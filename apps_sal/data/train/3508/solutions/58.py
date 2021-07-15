def halving_sum(n): 
    suma = 0
    sumando = n
    while sumando >= 1:
        suma = suma+ sumando
        sumando = sumando //2
    return suma
