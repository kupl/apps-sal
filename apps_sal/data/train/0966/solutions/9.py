t = int(input())
for i in range(t):
    n, u, d = list(map(int, input().split()))
    h = list(map(int, input().split()))
    flag = 0
    flag1 = 0
    c = 0
    for i in range(n - 1):
        if(h[i + 1] > h[i] and (h[i + 1] - h[i]) <= u):
            pass
        elif(h[i + 1] > h[i] and (h[i + 1] - h[i]) > u):
            c = i
            break
        elif(h[i + 1] < h[i]):
            if((h[i] - h[i + 1]) > d):
                if(flag == 0):
                    flag = 1
                    pass
                else:
                    c = i
                    break
            elif(h[i] - h[i + 1] <= d):
                pass
        if(i == n - 2):
            flag1 = 1
            break
    if(flag1 == 0):
        print(c + 1)
    elif(flag1 == 1):
        print(n)
