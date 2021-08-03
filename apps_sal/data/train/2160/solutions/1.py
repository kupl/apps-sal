n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
val = sum(arr)
if(val % k != 0):
    print('No')
else:
    flag = 0
    i = 0
    arr1 = []
    sumx = 0
    count = 0
    while(i < n):
        sumx += arr[i]
        count += 1
        if(sumx == val // k):
            arr1.append(count)
            sumx = 0
            count = 0
        elif(sumx > val // k):
            flag = 1
            break
        i += 1
    if(flag == 1):
        print('No')
    else:
        print('Yes')
        print(*arr1)
