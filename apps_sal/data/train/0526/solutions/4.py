for _ in range(int(input())):
    s = input()
    n = len(s)
    if n == 1:
        if s[0].isalpha():
            print("-32")
        else:
            print(0)
    else:
        num, ch = 0, 0
        p, q = 0, 0
        c = 1
        x = s[0]
        ans = ""
        for i in range(1, n):
            if s[i - 1] == s[i]:
                c += 1
                if i == n - 1:
                    ans += s[i]
                    if s[i].isalpha():
                        ch += 1
                    else:
                        num += 1
                    if c > 1:
                        ans += str(c)
                        num += 1
                    c = 1

            else:
                if s[i - 1].isalpha():
                    ch += 1
                    ans += s[i - 1]
                    if c > 1:
                        ans += str(c)
                        num += 1
                    c = 1
                else:
                    ans += s[i - 1]
                    num += 1
                    if c > 1:
                        ans += str(c)
                        num += 1
                    c = 1
                if i == n - 1:
                    ans += s[i]
                    if s[i].isalpha():
                        ch += 1
                    else:
                        num += 1
        alp, qt = 0, 0
        for i in range(n):
            if s[i].isalpha():
                alp += 1
            else:
                qt += 1
        sol = ((qt - num) * 32) + ((alp - ch) * 8)
        print(sol)
