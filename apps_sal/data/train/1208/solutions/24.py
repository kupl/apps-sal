n = 100000
m = 1000000007
a = [0] * n
a[0] = 1
fib = 1
for i in range(2, n - 200):
    fib = fib * i % m
    a[i - 1] = a[i - 2] * fib % m
for _ in range(int(input())):
    n = int(input())
    print(a[n - 1])
