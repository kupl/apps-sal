import math
t = int(input())
for you in range(t):
    n = int(input())
    z = int(math.sqrt(n))
    l = [z - 1, z - 2, z, z + 1, z + 2]
    mina = 10 ** 18
    for i in l:
        if i > 0:
            mina = min(mina, i + (n + i - 1) // i - 2)
    print(mina)
