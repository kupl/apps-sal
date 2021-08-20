s = input()
if 'c' in s or 'k' in s:
    print(0)
else:
    l1 = []
    pre = s[0]
    count = 1
    for i in s[1:]:
        if pre == i and i in 'gf':
            count += 1
        else:
            if count != 1:
                l1.append(count)
            count = 1
        pre = i
    if count > 1:
        l1.append(count)
    ans = 1
    for t in l1:
        ans *= (t * t - 3 * t + 6) / 2
    print(int(ans))
