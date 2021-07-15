def binary_pyramid(m,n):
    suma = []
    for i in range(m,n+1):
        suma.append(int(bin(i)[2:]))
    return bin(sum(suma))[2:]
