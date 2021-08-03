s = input()
ans = [0 for i in range(len(s))]
lp = 0
rp = len(s) - 1
for i in range(len(s)):
    if s[i] != 'l':
        ans[lp] = i + 1
        lp += 1
    else:
        ans[rp] = i + 1
        rp -= 1
for i in ans:
    print(i)
