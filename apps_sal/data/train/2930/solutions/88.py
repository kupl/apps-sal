def summation(num):
    if isinstance(num, int) and num > 0:
        s = 0
        for i in range(num):
            s = s + i
        return s + num
    else:
        print('No es un número entero positivo')
