# cook your dish here
for i in range(int(input())):
    n, k = [int(i) for i in input().split()]
    arr = [k**int(i) for i in input().split()]
    v1 = sum(arr)
    v1 = v1 // 2
    v2 = 0
    for i in range(len(arr)):
        v2 += arr[i]
        if(v2 >= v1):
            break
    if(i == 0):
        print(1)
    else:
        if(abs(v2 - v1) < abs(v2 - arr[i] - v1)):
            print(i + 1)
        else:
            print(i)
