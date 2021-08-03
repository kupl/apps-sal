s = input()
ans = 0
for i in range(0, len(s) - 1):
    addQ = 0
    subQ = 0
    cur = 0
    for j in range(i, len(s)):
        if s[j] == '(':
            cur += 1
        elif s[j] == ')':
            cur -= 1
            if cur < 0 and subQ > 0:
                cur += 2
                subQ -= 1
                addQ += 1
        else:
            if cur > 0:
                subQ += 1
                cur -= 1
            else:
                addQ += 1
                cur += 1
        if cur < 0:
            break
        if cur == 0:
            ans += 1
print(ans)
