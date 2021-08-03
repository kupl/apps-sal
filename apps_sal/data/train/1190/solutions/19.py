# cook your dish here
t = int(input())
for t in range(t):
    P = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    n = int(input())
    count = 0
    for i in P:
        if(n >= i):
            count = count + n // i
            n = n % i
    print(count)
