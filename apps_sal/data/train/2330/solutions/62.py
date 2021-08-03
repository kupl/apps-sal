s = list(input())
n = len(s)
if s[0] == '0' or s[-1] == '1':
    print((-1))
else:
    s.pop()
    sr = s.copy()
    sr.reverse()
    if s != sr:
        print((-1))
    else:
        ans = []
        now = 1
        cnt = 1
        for x in s:
            if x == '1':
                ans.append([now, now + cnt])
                now += cnt
                cnt = 1
            else:
                ans.append([now, now + cnt])
                cnt += 1
        for x in ans:
            print((x[0], x[1]))
