def solve(s):
    s = s.split(" ")
    temp = []
    result = []
    for l in s:
        temp.append(len(l))

    s = ''.join(s)
    s = s[::-1]

    for x in temp:
        add = s[:x]
        s = s[x:]
        result.append(add)

    a = ""
    for i in result:
        a += i + " "
    a = a[:-1]

    return a
