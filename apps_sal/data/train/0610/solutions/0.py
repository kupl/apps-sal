t = int(input())
while t > 0:
    n = int(input())
    l = list(map(int, input().split()))
    l1 = []
    c = 1
    for i in range(len(l)):
        if l[i] == 1:
            l1.append(i)
    for j in range(len(l1) - 1):
        if l1[j + 1] - l1[j] < 6:
            c = 0
            break
    if c:
        print('YES')
    else:
        print('NO')
    t -= 1
