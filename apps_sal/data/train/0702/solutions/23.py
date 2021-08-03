t = int(input())
flag = 0
for i in range(t):
    m, tc, th = map(int, input().split())

    # for j in range(m):
    #     tc+=2
    #     th-=1
    #     if(tc==th):
    #         flag=1
    #         print('No')
    #         break
    #     if(tc>th):
    #         flag=0
    #         break

    # if(flag==0):
    #     print('Yes')
    new_m = (th - tc) / 3
    m2 = int(new_m)
    if(new_m <= m and new_m == m2):
        print('No')
    else:
        print('Yes')
