n, k = list(map(int, input().split()))
t = set(map(int, input().split()))
y = x = min(t)
t = list(t)
while True:
    for i in t:
        if i % x > k:
            x = i // (i // x + 1)
    if y == x:
        break
    y = x
print(y)
