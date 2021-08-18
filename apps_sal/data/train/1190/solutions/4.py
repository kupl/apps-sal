t = int(input())
l = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
for i in range(t):
    n = int(input())
    r = 0
    while(n > 0):
        for j in l:
            if(n >= j):
                r += n // j
                n %= j
    print(r)
