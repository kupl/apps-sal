# cook your dish here
t = int(input())
for i in range(t):
    P = [100, 50, 10, 5, 2, 1]
    n = int(input())
    count = 0
    for i in P:
        if(n >= i):
            count = count + n // i
            n = n % i
    print(count)
