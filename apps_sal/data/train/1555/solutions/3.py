t = int(input())
for i in range(t):
    n = int(input())
    if(n == 1):
        print(n)
    elif(n < 0):
        print(0)
    else:
        print((((n - 1) * (n - 1)) + (n * n * n)) % 1000000007)
