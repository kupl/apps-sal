t = int(input())
for i in range(t):
    n = int(input())
    s = n ** 3 + (n - 1) ** 2
    print(s % 1000000007)
