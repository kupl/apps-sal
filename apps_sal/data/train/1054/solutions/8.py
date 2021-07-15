# cook your dish here
t = int(input())

while t > 0:
    t -= 1
    s = list(input())
    res = True
    l = 0
    r = len(s)-1
    while l <= r:
        if s[l].isalpha() and s[r].isalpha():
            if s[l] != s[r]:
                res = False
                break
        elif s[l] == '.' and s[r] == '.':
            s[l] = 'a'
            s[r] = 'a'
        elif s[l] == '.':
            s[l] = s[r]
        else:
            s[r] = s[l]
        l += 1
        r -= 1
    if res:
        print("".join(s))
    else:
        print(-1)


