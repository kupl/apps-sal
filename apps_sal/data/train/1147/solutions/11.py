for _ in range(int(input())):
    n = int(input())
    s = input()
    dic = dict()
    for i in range(n):
        dic[s[i]] = dic.setdefault(s[i], 0) + 1
    ans = 0
    for i in dic:
        if dic[i] % 2 != 0:
            ans += 1
    print(ans - 1 if ans > 0 else ans)
