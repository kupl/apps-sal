t = int(input())
flag = 0
for i in range(t):
    m, tc, th = map(int, input().split())

    new_m = (th - tc) / 3
    m2 = int(new_m)
    if(new_m <= m and new_m == m2):
        print('No')
    else:
        print('Yes')
