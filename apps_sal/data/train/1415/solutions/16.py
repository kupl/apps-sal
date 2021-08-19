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
    f = 0
    if is_pal(s):
        print('YES')
    else:
        for j in range(len(s)):
            c.append(s[j])
            d.append(s[j])
        n = len(s)
        for j in range(n):
            if s[j] != s[n - j - 1]:
                c.pop(j)
                x = is_pal(c)
                if x == 1:
                    f = 1
                    break
                else:
                    c.clear()
                    for i in range(len(d)):
                        c.append(d[i])
                    c.pop(n - j - 1)
                    x = is_pal(c)
                    if x == 1:
                        f = 1
                        break
                    else:
                        c.clear()
                        for i in range(len(d)):
                            c.append(d[i])
        if f == 1:
            print('YES')
        else:
            print('NO')
