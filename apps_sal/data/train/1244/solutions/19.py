s = 0
n = int(input())
while(n):

    mod = int(1e9 + 7)
    a, b = [int(x) for x in input().split()]
    s += abs(b - a) + 1
    s %= mod
    n -= 1
print(s)
