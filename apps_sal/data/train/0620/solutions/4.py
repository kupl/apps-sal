t = int(input())
while t:
    a = input().split()
    n = int(a[0])
    k = int(a[1])
    lst = input().split()
    for i in range(n):
        lst[i] = int(lst[i])
    greater = 0
    length = 0
    pos = -1
    allTimeLong = 0
    for i in range(n):
        if lst[i] > k and greater != 0 and (lst[i] != greater):
            greater = lst[i]
            if allTimeLong < length:
                allTimeLong = length
            length = i - pos
            pos = i
            continue
        elif lst[i] > k:
            greater = lst[i]
            pos = i
        length += 1
    if allTimeLong < length:
        allTimeLong = length
    t -= 1
    print(allTimeLong)
