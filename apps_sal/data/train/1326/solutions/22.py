t = int(input())
for i in range(t):
    n = int(input())
    f = list(map(int, input().strip().split()))
    current_gasoline = 0
    dist = 0
    for cars in range(1, n + 1):
        current_gasoline += f[cars - 1]
        if current_gasoline == 0:
            break
        f[cars - 1] = 0
        dist += 1
        current_gasoline -= 1
    dist += current_gasoline
    print(dist)
