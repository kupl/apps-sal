def collatz_steps(n, s):
    while True:
        x = n
        ans = ''
        flag = True
        for j in range(len(s)):
            if x % 2 == 0:
                x = x // 2
                ans += 'D'
            else:
                x = (x * 3 + 1) // 2
                ans += 'U'
            if ans[j] != s[j]:
                flag = False
                break
        if flag == True:
            return n
        else:
            n += 2 ** (len(ans) - 1)
