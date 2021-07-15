binary_pyramid=lambda m,n:bin(sum(int(bin(e)[2:]) for e in range(m,n+1)))[2:]
