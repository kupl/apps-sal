t = int(input())
for i in range(0, t):
    l = []
    N = int(input())
    for j in range(0, N):
        x = input()
        l.append(x)
    print(int(N * (N + 1) / 2))
