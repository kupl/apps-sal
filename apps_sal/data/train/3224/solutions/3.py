def binary_pyramid(m, n): return bin(sum(int(bin(e)[2:]) for e in range(m, n + 1)))[2:]
