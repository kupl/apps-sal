T = int(input())
t = []
for _ in range(T):
    N = int(input())
    t.append(N)
N = max(t) + 1
l = [0 for i in range(N)]
p = 1
a = 1
for i in range(1, N):
    a = (a * i) % 1000000007
    p = p * a % 1000000007
    l[i] = p
for i in t:
    print(l[i])
