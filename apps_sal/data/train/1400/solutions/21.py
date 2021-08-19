for _ in range(int(input())):
    (n, l, r) = list(map(int, input().split()))
    temp = [1]
    temp1 = [1]
    t = 1
    m = 1
    count = 1
    for i in range(n - 1):
        if count < l:
            m = m * 2
            temp.append(m)
        else:
            temp.append(1)
        if count < r:
            t = t * 2
            temp1.append(t)
        else:
            temp1.append(max(temp1))
        count = count + 1
    print(sum(temp), sum(temp1))
