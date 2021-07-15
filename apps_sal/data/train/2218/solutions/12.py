import sys

input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))
check = [-1] * n
maxx = 0
for i in [input().split() for i in range(int(input()))][::-1]:
    if i[0] == '2':
        maxx = max(maxx, int(i[1]))
    else:
        if check[int(i[1]) - 1] == -1:
            check[int(i[1]) - 1] = max(int(i[2]), maxx)
for i in range(n):
    if check[i] == -1:
        check[i] = max(maxx, li[i])
print(*check)

