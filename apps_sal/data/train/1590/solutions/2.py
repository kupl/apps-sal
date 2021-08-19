test = int(input())
while test != 0:
    a = list(map(int, input().split()))
    a.sort()
    if a[0] + a[1] + 1 >= max(a):
        print('Yes')
    else:
        print('No')
    test -= 1
