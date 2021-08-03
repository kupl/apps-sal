MOD = 1000000007

t = eval(input())
t = int(t)
while(t > 0):
    t = t - 1
    n = eval(input())
    n = int(n)
    m = n
    result = 1
    x = 3
    while(n > 0):
        if(n & 1):
            result = (result * x) % MOD
        x = (x * x) % MOD
        n = n >> 1
    if(m % 2 == 1):
        print(result - 3)
    else:
        print((result + 3) % MOD)
