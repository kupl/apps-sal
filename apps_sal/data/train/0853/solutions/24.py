T = int(input())
for _ in range(T):
    N = int(input())
    l = []
    for i in range(N):
        name = input()
        time = int(input())
        l.append((name, time))
    l = sorted(l, key=lambda ele: ele[1])
    for j in range(N):
        print(l[j][0])
