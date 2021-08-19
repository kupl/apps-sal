(n, a, b) = map(int, input().split())
x = list(map(int, input().split()))
now = x[0]
fatigue = 0
for v in x:
    if a * (v - now) < b:
        fatigue += a * (v - now)
    else:
        fatigue += b
    now = v
print(fatigue)
