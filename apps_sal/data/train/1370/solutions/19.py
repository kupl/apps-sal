# cook your dish here
try:
    t = int(input())
except:
    t = 0
for i in range(t):
    X = list(map(int, input().split()))
    r = X[0] % 10
    q = (X[0] % 100 - r) / 10
    p = (X[0] - q * 10 - r) / 100
    N = [0] * 10
    N[int(p)] += 1
    N[int(q)] += 1
    N[int(r)] += 1
    ans = 4 - max(N)
    print(ans**3)
