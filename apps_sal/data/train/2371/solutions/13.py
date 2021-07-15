for _ in range(int(input())):
    n = int(input())
    a = input().split(' ')
    for i in range(n):
        a[i] = int(a[i])
    i = n-1
    while i > 0:
        if a[i] <= a[i-1]:
            i -= 1
            continue
        else:
            break
    while i > 0:
        if a[i] >= a[i-1]:
            i -= 1
            continue
        else:
            break
    print(i)

