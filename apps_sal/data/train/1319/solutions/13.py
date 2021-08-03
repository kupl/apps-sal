n, m = map(int, input().split())

lis = []
for i in range(n + m):
    k = int(input())
    if k == -1:
        lis.sort()
        print(lis.pop())

    else:
        lis.append(k)
