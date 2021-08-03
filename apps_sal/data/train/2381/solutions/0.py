for i in range(int(input())):
    s = 'R' + input() + 'R'
    prev = 0
    ma = -1
    for i in range(1, len(s)):
        if s[i] == 'R':
            ma = max(ma, i - prev)
            prev = i
    print(ma)
