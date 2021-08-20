t = int(input())
for i in range(t):
    c = 0
    n = int(input())
    a = [int(j) for j in input().split()]
    b = [int(j) for j in input().split()]
    a.sort()
    b.sort()
    for j in range(len(a)):
        if a[j] < b[j]:
            c += a[j]
        else:
            c += b[j]
    print(c)
