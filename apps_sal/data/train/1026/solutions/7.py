m = 10**9 + 7
t = int(input())
for i in range(t):
    ls = list(map(int, input().split()))
    ls.sort()
    print((ls[0] * (ls[1] - 1) * (ls[2] - 2)) % m)
