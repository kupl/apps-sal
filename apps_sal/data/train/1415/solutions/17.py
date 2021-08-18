def is_pal(s):
    if len(s) == 1:
        return 1
    else:
        count = 0
        for i in range(int(len(s) / 2)):
            if s[i] == s[len(s) - 1 - i]:
                count += 1
        if count == int(len(s) / 2):
            return 1
        else:
            return 0


t = int(input())
for i in range(t):
    count = 0
    s = input()
    c = list()
    d = list()
    for j in range(len(s)):
        c.append(s[j])
        d.append(s[j])
    for j in range(len(s)):
        c.pop(j)
        x = is_pal(c)
        if x == 1:
            print('YES')
            break
        else:
            count += 1
            c.clear()
            for i in range(len(d)):
                c.append(d[i])
    if count == len(s):
        print('NO')
