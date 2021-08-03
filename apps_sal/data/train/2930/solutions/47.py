def summation(num):
    nombre = num
    sum_interm = 0
    while nombre > 0:
        sum_interm = sum_interm + nombre
        nombre -= 1
    return sum_interm
