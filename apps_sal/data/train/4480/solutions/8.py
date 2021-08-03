def parse(s):
    ans = []
    num = 0
    for c in s:
        if c == 'i':
            num += 1
        if c == 'd':
            num -= 1
        if c == 's':
            num **= 2
        if c == 'o':
            ans.append(num)
    return ans
