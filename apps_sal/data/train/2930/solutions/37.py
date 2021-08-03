def summation(num):
    if num < 1:
        print("El número debe ser mayor a 0")
    else:
        cont = 0
        total = 0
        while cont <= num:
            total = total + cont
            cont = cont + 1

        return total
