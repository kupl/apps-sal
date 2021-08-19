N = int(input())
for i in range(N):
    p = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    a = int(input())
    count = 0
    for i in p:
        if a >= i:
            count = count + a // i
            a = a % i
    print(count)
