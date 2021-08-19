for _ in range(int(input())):
    (s, k) = map(str, input().split())
    s1 = list(set(s))
    k = int(k)
    ans = ''
    for i in range(97, 123):
        if chr(i) in s1:
            if k > 0:
                ans += chr(i)
                k -= 1
            else:
                continue
        else:
            ans += chr(i)
    if len(s1) <= len(ans):
        print(ans[:len(s1)])
    else:
        print('NOPE')
