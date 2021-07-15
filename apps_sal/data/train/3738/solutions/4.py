FIB = [0, 1]
for _ in range(1000): FIB.append(FIB[-2] + FIB[-1])

def calc(k, n, m, x):
    l = (m - (FIB[n-3] + 1) * k) // (FIB[n-2] - 1)
    return (FIB[x-2] + 1) * k + (FIB[x-1] - 1) * l
