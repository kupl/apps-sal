t = int(input())
for t1 in range(t):
    b = input()
    a = list(map(int, input().split()))
    x = 0
    f = 0
    while x < len(a) - 2:
        if a[x] == a[x + 1] and a[x + 1] == a[x + 2]:
            f = 1
            break
        x += 1
    if f == 1:
        print('Yes')
    else:
        print('No')
