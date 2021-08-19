def binary_pyramid(a, b):
    return bin(sum((int(bin(n)[2:]) for n in range(a, b + 1))))[2:]
