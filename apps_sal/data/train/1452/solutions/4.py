T = int(input())
for _ in range(T):
    N, M = list(map(int, input().split()))
    robots = [0] * N
    c = 0
    Id = M
    while robots[Id] != 1:
        robots[Id] = 1
        c += 1
        Id = (Id + M) % N
    if c == N:
        print("Yes")
    else:
        print("No", c)
