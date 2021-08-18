for i in range(int(input())):
    a, b = [int(i) for i in input().split()]
    l1 = [int(i) for i in input().split()]
    l2 = [int(i) for i in input().split()]
    l = []
    for i in range(a * b):
        if(l1[i] > l2[i]):
            l.append([l1[i], 1])
        else:
            l.append([l2[i], 2])
    l.sort()
    arr = []
    for i in range(a * b):
        if(l[i][1] == 1):
            arr.append(i + 1)
    j = 1
    ans = 0
    for i in range(len(arr)):
        if(arr[i] >= j * b):
            ans += 1
            j += 1
    print(ans)
