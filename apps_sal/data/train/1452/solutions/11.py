for i in range(int(input())):
    l = [int(j) for j in input().split()]
    n, m = l[0], l[1]
    count = 0
    j = 1
    while j <= n:
        j = j + m
        if j > n:
            j = j - n
        count += 1
        if j == 1:
            break
    if count == n:
        print('Yes')
    else:
        print('No ' + str(count))
