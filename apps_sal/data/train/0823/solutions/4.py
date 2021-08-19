def ss(a, su, i, cnt):
    if su == 0 and cnt != 0:
        return 1
    if i < 0:
        return 0
    return ss(a, su + a[i], i - 1, cnt + 1) + ss(a, su, i - 1, cnt)


for _ in range(int(input())):
    a = [int(x) for x in input().split()]
    if ss(a, 0, 3, 0):
        print('Yes')
    else:
        print('No')
