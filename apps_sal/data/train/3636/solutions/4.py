def bouncy_ratio(percent):
    ans = 0
    for i in range(1, 10**10):
        s = str(i)
        res = ''.join(['=' if a == b else '>' if int(a) > int(b) else '<' for a, b in zip(s, s[1:])])
        ans += ('<' in res) and ('>' in res)
        if ans / i >= percent:
            return i
