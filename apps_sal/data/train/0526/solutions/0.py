# include<sdg.h>
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
                    ans += s[i - 1]
                    ch += 1
                    if c > 1:
                        ans += str(c)
                        num += 1
                    c = 1
            else:
                ans += s[i - 1]
                ch += 1
                if c > 1:
                    ans += str(c)
                    num += 1
                c = 1
                if i == n - 1:
                    ans += s[i]
                    ch += 1
        # print(ans,num,ch)
        sol = (n * 8) - ((num * 32) + (ch * 8))
        print(sol)
