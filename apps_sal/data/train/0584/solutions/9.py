for _ in range(int(input())):
    s = input().strip()
    if s[0] == '0' or '1' not in s:
        print(0)
    else:
        ans = 0
        s = s.lstrip('1')
        for i in range(len(s)):
            if s[i] == '1':
                break
            ans += 1
        print(ans)

