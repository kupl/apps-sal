ile = eval(input())
while ile:
    suma = 0
    lista = input()
    jeweled = input()
    for znak in jeweled:
        if znak in lista:
            suma += 1
    print(suma)
    ile -= 1
