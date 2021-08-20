(a, b, c) = map(int, input().split())
n = 0
for i in range(a):
    t = list(map(int, input().split()))
    d = t[-1]
    t.pop(-1)
    if d <= 10 and sum(t) >= b:
        n += 1
print(n)
