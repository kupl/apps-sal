def findTransitionPoint(arr, n):
    lb = 0
    ub = n - 1

    while (lb <= ub):

        mid = (int)((lb + ub) / 2)
 
        if (arr[mid] == 0):
            lb = mid + 1

        elif (arr[mid] == 1):

            if (mid == 0 \
                or (mid > 0 and\
                arr[mid - 1] == 0)):
                return mid

            ub = mid-1
     
    return -1
 

for _ in range(int(input())):
    n = int(input())
    nn = list(map(int,input().split(" ")))
    nn = sorted(nn)
    # res = 0
    # for ele in nn: 
    #     res = (res << 1) | ele 
    # print(res)


    arr = nn
    n = len(arr)
    point = findTransitionPoint(arr, n);
    print(point)
    
