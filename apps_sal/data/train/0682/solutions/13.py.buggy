n = int(input())
l = list(map(int, input().split()))
flag = 0
for i in range(1, n + 1):
    if l[i - 1] != i:
        start = i
        flag = 1
        break
for i in range(n, 0, -1):
    if l[i - 1] != i:
        end = i
        break
if flag == 0:
    print(0, 0)
    return
for x in range(start - 1, end - 1):
    if l[x + 1] != l[x] - 1:
        print(0, 0)
        return
print(start, end)
