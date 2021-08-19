def idat(pos, M, N):
    return (pos + M) % N


T = eval(input())
for _ in range(T):
    N, M = list(map(int, input().split(" ")))
    robots = [0] * N
#     print range(1,N+1)[M:]+range(1,N+1)[:M]
    Id = idat(0, M, N)
    while robots[Id] != 1:
        robots[Id] = 1
        newpos = Id
        Id = idat(newpos, M, N)
#         print robots[M:]+robots[:M]
    if robots.count(1) == N:
        print("Yes")
    else:
        print("No", robots.count(1))
