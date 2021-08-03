T = int(input())
for i in range(T):
    N = int(input())
    F = input().split()
    Gas = int(F[0])
    Distance = 0
    while Gas != 0:
        Distance += 1
        try:
            Gas = Gas + int(F[Distance]) - 1
        except:
            Gas -= 1
    print(Distance)
