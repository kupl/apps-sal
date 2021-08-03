for i in range(int(input())):
    s = input()
    one = [0] * (len(s) + 1)  # number of ones from first place to i-th place
    for i in range(len(s)):
        if s[i] == '1':
            one[i + 1] = one[i] + 1
        else:
            one[i + 1] = one[i]
    ans = 0
    i = 1
    r = 2  # r for range in interval r=i+i**2
    while r <= len(s):
        r = i + i**2
        j = 0
        while j <= len(s) - r:
            if one[j + r] - one[j] == i:
                ans += 1
                j += 1
            else:
                j += abs(i - (one[j + r] - one[j]))
        i += 1
    print(ans)
