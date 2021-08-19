# cook your dish here
t = int(input())
while(t):
    n = int(input())
    arr = list(map(int, input().strip().split(' ')))
    pre = []
    suff = [0] * n
    pre.append(1)
    for i in range(1, n):
        if(arr[i] > arr[i - 1] and pre[i - 1] == 1):
            pre.append(1)
        else:
            pre.append(0)
    flag = 0
    temp = 0
    for i in range(n - 1, -1, -1):
        if(i == n - 1):
            suff[i] = 1
        elif(arr[i] < arr[i + 1] and suff[i + 1] == 1):
            suff[i] = 1
        else:
            if(flag == 0):
                temp = i + 1
                # print(temp)
                suff[i] = 0
                flag = 1
            else:
                suff[i] = 0
                # flah=1

    #print(pre,end=' ')
    # print()
    # print(suff,end='')
    # print(temp)
    count = 0
    for i in range(n):
        if(pre[i] == 1):
            count += 1
            for j in range(temp, n):
                if(arr[j] > arr[i] and j > i + 1):
                    count += (n - j)
                    # print(n-j)
                    break
    count += (n - temp)
    if(pre[temp] == 1):
        count -= 2
    print(count)
    t -= 1
