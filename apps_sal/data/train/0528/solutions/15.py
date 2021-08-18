def nextPowerOf2(n):
    count = 0

    if (n and not(n & (n - 1))):
        return n

    while(n != 0):
        n >>= 1
        count += 1

    return 1 << count


T = int(input())
for i in range(0, T):
    N, L = list(map(int, input().split()))
    l = 1
    j = N**l
    if(N == 1):
        print(L)
    elif(N == 2):
        n = nextPowerOf2(L)
        print(n)
