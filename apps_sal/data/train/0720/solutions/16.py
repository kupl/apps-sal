for _ in range(int(input())):
    s = input()
    a = []
    a.append(0)
    count = 1
    for i in s:
        if i == '1':
            a.append(a[-1] + 1)
        else:
            a.append(a[-1])
        count += 1
    ans = 0
    i = 1
    r = 2
    while r < count:
        j = 0
        while j < count - r:
            if a[j + r] - a[j] == i:
                ans += 1
                j += 1
            else:
                j += abs(i - (a[j + r] - a[j]))
        i += 1
        r = i + i**2
    print(ans)
