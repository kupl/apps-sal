T = int(input())
for i in range(0, T):
    N = int(input())
    L = []
    for j in range(0, N):
        (x, y) = list(map(int, input().split()))
        L.append((x, y))
    arr11 = []
    arr12 = []
    for j in range(0, len(L)):
        arr11.append(L[j][1] - L[j][0])
        arr12.append(L[j][1] + L[j][0])
    arr11 = sorted(arr11)
    arr12 = sorted(arr12)
    arr11 = arr11[::-1]
    arr12 = arr12[::-1]
    arr21 = [100000000000]
    arr22 = [100000000000]
    for j in range(0, len(L) - 1):
        arr21.append(arr11[j] - arr11[j + 1])
        arr21.append(arr12[j] - arr12[j + 1])
    print(min(min(arr21), min(arr22)) / 2)
