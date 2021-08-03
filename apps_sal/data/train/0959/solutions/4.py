n = int(input())
l = []
for i in range(0, n):
    a = int(input())
    x = list(map(int, input().split()))
    x.sort()
    total = 0
    b = a // 2
    for j in range(0, b):
        total = total + abs(x[a - j - 1] - x[j])
    l.append(total)
for i in l:
    print(i)
