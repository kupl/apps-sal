(n, m) = map(int, input().split())
iArr = []
for _ in range(n + m):
    i = int(input())
    if i != -1:
        iArr.append(i)
    else:
        print(max(iArr))
        iArr.remove(max(iArr))
