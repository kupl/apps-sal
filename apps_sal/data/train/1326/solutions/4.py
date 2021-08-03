t = 0
t = int(input())

for i in range(0, t):
    n = 0
    n = int(input())
    f = []
    f = list(map(int, input().split()))

    total_fuel = f[0]
    total_dist = 0
    i = 1

    while(total_fuel > 0 and total_dist <= n - 1 and i <= n - 1):
        total_fuel = total_fuel + f[i] - 1
        total_dist = i
        i = i + 1

    if(total_fuel == 0):
        ans = total_dist
    else:
        ans = total_fuel + total_dist

    print(ans)
