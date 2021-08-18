t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    m = int(input())
    b = [int(x) for x in input().split()]
    i = j = c = 0
    while i < n and j < m:
        if b[j] == a[i]:
            j += 1
            i += 1
            c += 1
        else:
            i += 1
    if c == m:
        print('Yes')
    else:
        print('No')
