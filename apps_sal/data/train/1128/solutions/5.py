def sum_ar(arr, len):
    if (len == 0):
        return 0
    else:
        return arr[len - 1] + sum_ar(arr, len - 1)


t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int, input().split()))
    check = False
    for i in range(0, len(li), 1):
        sli1 = sum_ar(li[0:i], len(li[0:i]))
        sli2 = sum_ar(li[i + 1:len(li)], len(li[i + 1:len(li)]))
        if(sli1 == sli2):
            check = True
            break
    if(check):
        print(i)
    else:
        print(-1)
