t = int(input())
for i in range(0, t):
    n = int(input())
    l1 = list(map(int, input().split()))
    l1.sort()
    l1[-1] = 0
    sum1 = 0
    for a in l1:
        sum1 += a
    l2 = list(map(int, input().split()))
    l2.sort()
    l2[-1] = 0
    sum2 = 0
    for b in l2:
        sum2 += b
    if sum1 < sum2:
        print('Alice')
    elif sum1 > sum2:
        print('Bob')
    else:
        print('Draw')
