def binary_pyramid(m,n):
    return bin(sum(eval(bin(i)[2:]) for i in range(m, n+1)))[2:]
