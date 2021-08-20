(n, m) = map(int, input().split())
lis = []
for i in range(n + m):
    k = int(input())
    if k == -1:
        print(str(max(lis)))
        lis.remove(max(lis))
    else:
        lis.append(k)
