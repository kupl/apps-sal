n = int(input())
a = list(map(int, input().split()))
m = int(input())
l = []
for i in range(m):
    x = int(input())
    l.append(a.pop(x - 1))
for j in l:
    print(j)
