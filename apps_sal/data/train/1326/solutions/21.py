t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    d = 0
    fuel = 0
    for i in range(n):
        fuel += arr[i]
        if fuel == 0:
            break
        d += 1
        fuel -= 1
    if fuel == 0:
        print(d)
    else:
        print(d + fuel)
