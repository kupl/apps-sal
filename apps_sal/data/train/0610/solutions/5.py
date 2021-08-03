# cook your dish here
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    # 101 --- 1000001 ----
    f = True
    for i in range(n):
        if(l[i] == 1):
            if(i + 1 < n):
                if(l[i + 1] == 1):
                    f = False
                    break
            if(i + 2 < n):
                if(l[i + 2] == 1):
                    f = False
                    break
            if(i + 3 < n):
                if(l[i + 3] == 1):
                    f = False
                    break
            if(i + 4 < n):
                if(l[i + 4] == 1):
                    f = False
                    break
            if(i + 5 < n):
                if(l[i + 5] == 1):
                    f = False
                    break
    if(f == True):
        print('YES')
    else:
        print('NO')
