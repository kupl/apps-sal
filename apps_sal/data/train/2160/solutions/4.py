n, k = map(int, input().split())
arr = list(map(int, input().split()))
l = sum(arr)

if l % k == 0:
    count = l // k
    a = [-1] * (k + 1)
    j = 1
    i = 0
    ptr1 = 0
    flag = 0
    while(i < k):
        temp = 0
        while(ptr1 < n):
            temp += arr[ptr1]
            if temp == count:
                a[j] = ptr1
                j += 1
                ptr1 += 1
                break
            elif temp > count:
                flag = 1
                break
            ptr1 += 1
        if temp < count:
            flag = 1
        if flag == 1:
            break
        i += 1
    if flag == 1:
        print("No")
    else:
        print("Yes")
        for i in range(1, k + 1):
            print(a[i] - a[i - 1], end=" ")
        print()
else:
    print("No")
