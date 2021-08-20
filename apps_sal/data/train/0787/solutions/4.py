for _ in range(int(input())):
    s = input()
    count = 0
    n = len(s)
    count = 0
    total = 0
    lastindex = n - 1
    curr = n - 1
    while curr >= 0 and s[lastindex] == '1':
        curr -= 1
        lastindex -= 1
    while curr >= 0:
        if s[curr] == '1':
            if s[curr + 1] == '0':
                count += 1
            total += count + (lastindex - curr)
            lastindex -= 1
        curr -= 1
    print(total)
