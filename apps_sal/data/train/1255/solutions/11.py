for _ in range(int(input())):
    (s, k) = map(str, input().split())
    k = int(k)
    if 26 - len(s) + k < len(s):
        print('NOPE')
    else:
        (k1, ans) = (k, '')
        for i in range(97, 123):
            a = chr(i)
            if s.count(a) > 0:
                if k1 > 0:
                    k1 -= 1
                    ans += a
            else:
                ans += a
            if len(ans) == len(s):
                break
        print(ans)
