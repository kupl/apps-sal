n, a, b = map(int, input().split())
x = list(map(int, input().split()))

current = x[0]
cost = 0
for i in x:
    if (i - current) * a <= b:
        cost += (i - current) * a
        current = i
    else:
        cost += b
        current = i
print(cost)
