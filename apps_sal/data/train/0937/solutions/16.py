# cook your dish here
for _ in range(int(input())):
    s = input()
    n = len(s)
    ans = "yes"
    st = "CES"
    if n == 1:
        print(ans)
        continue
    elif n == 2:
        for i in range(0, 1):
            curr = s[i]
            if curr == 'C' and (s[i + 1] == 'C' or s[i + 1] == 'E' or s[i + 1] == 'S'):
                continue
            elif curr == 'E' and (s[i + 1] == 'E' or s[i + 1] == 'S'):
                continue
            elif curr == 'S' and s[i + 1] == 'S':
                continue
            else:
                ans = "no"
                break

    else:
        for i in range(0, n - 2):
            curr = s[i]
            if curr == 'C' and (s[i + 1] == 'C' or s[i + 1] == 'E' or s[i + 1] == 'S'):
                continue
            elif curr == 'E' and (s[i + 1] == 'E' or s[i + 1] == 'S'):
                continue
            elif curr == 'S' and s[i + 1] == 'S':
                continue
            else:
                ans = "no"
                break
    print(ans)
