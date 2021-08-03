for _ in range(int(input())):
    s = input()
    curr = 0
    for i in range(len(s)):
        if(s[i].isdigit()):
            curr = curr + 32
        else:
            curr = curr + 8
    c = s[0]
    ans = s[0]
    count = 0
    d = dict()
    if(c.isdigit()):
        curr2 = 32
    else:
        curr2 = 8
    for i in range(len(s)):
        if(c == s[i]):
            count += 1
        else:
            c = s[i]
            if(count != 1):
                ans = ans + str(count)
                curr2 += 32
            ans = ans + str(s[i])
            if(s[i].isdigit()):
                curr2 += 32
            else:
                curr2 += 8
            count = 1
    if(count != 1):
        ans = ans + str(count)
        curr2 += 32
    print(curr - curr2)
