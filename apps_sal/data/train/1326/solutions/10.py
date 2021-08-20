for t in range(int(input())):
    N = int(input())
    f = list(map(int, input().split()))
    gas = f[0]
    distance = 0
    for _ in range(1, N):
        if gas == 0:
            break
        gas = gas - 1 + f[_]
        distance += 1
    print(distance + gas)
