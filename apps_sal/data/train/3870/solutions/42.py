def solve(s):
    sa = s.replace(" ", "")
    print(sa)
    ml = list(sa)[::-1]
    print(ml, 'kurw')
    y = 0
    for x in range(len(s)):
        if s[x] == ' ':
            print(s[x], 'coo')
            ml.insert(x + y, s[x])
#             y += 1

    print(s)
    print(s[::-1])
    print(ml)
    return ''.join(ml)
