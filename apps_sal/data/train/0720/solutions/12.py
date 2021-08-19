for i in range(int(input())):
    s = input()
    one = [0]
    for i in range(len(s)):
        one += [one[-1]]
        if s[i] == '1':
            one[-1] += 1
    ans = 0
    i = 1
    r = 2
    while r <= len(s):
        r = i + i ** 2
        j = 0
        while j <= len(s) - r:
            if one[j + r] - one[j] == i:
                ans += 1
                j += 1
            else:
                j += abs(i - (one[j + r] - one[j]))
        i += 1
    print(ans)
