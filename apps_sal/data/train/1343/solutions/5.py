# cook your dish here
t = int(input())
while t > 0:
    s = input()
    n = len(s)
    f = 0
    if n == 1:
        f = 0
    else:
        if len(s) % 2 == 0:
            if s[0:n // 2] == s[n // 2:]:
                f = 1
        else:
            l = (n + 1) // 2
            for i in range(l):
                if i == l - 1:
                    a = s[0: i] + s[i + 1: len(s)]
                    h = len(a) // 2
                    if a[0: h] == a[h: len(a)]:
                        f = 1
                        break
                    else:
                        f = 0
                        break
                if s[i] == s[l + i]:
                    pass
                else:
                    a = s[0:i] + s[i + 1:len(s)]
                    if a[0: len(a) // 2] == a[len(a) // 2: len(a)]:
                        f = 1
                        break
                    else:
                        a = s[0: l + i] + s[l + 1 + i: len(s)]
                        if a[0: len(a) // 2] == a[len(a) // 2:len(a)]:
                            f = 1
                            break
    if f == 0:
        print('NO')
    else:
        print('YES')
    t -= 1
