def nextPowerOf2(n, count):
    if (n and not(n & (n - 1))):
        return n
    while(n != 0):
        n >>= 1
        count += 1
    return 1 << count


for _ in range(int(input())):
    print(nextPowerOf2(int(input()), 0))
