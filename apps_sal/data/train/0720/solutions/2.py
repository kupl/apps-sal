for i in range(int(input())):
    s = input()
    n = len(s)
    one = [0] * (n + 1)
    for i in range(n):
        if s[i] == '1':
            one[i + 1] = one[i] + 1
        else:
            one[i + 1] = one[i]
    ans = 0
    i = 1
    r = 2
    while r <= n:
        r = i + i**2
        j = 0
        while j <= n - r:
            if one[j + r] - one[j] == i:
                ans += 1
                j += 1
            else:
                j += abs(i - (one[j + r] - one[j]))
        i += 1
    print(ans)
