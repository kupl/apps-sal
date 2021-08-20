for i in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = int(input())
    c = [int(i) for i in input().split()]
    x = []
    for j in c:
        if j in a:
            x.append(a.index(j))
    c = 0
    for j in range(len(x) - 1):
        if x[j] < x[j + 1]:
            c = c + 1
    if c == b - 1:
        print('Yes')
    else:
        print('No')
