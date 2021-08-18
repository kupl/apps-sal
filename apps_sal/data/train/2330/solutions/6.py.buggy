s = input()
if s[0] == '0':
    print(-1)
elif s[-1] == '1':
    print(-1)
else:
    l = len(s)
    for i in range(l - 1):
        if s[i] != s[l - i - 2]:
            print(-1)
            return
    ans = []
    base = 1
    for i in range(l - 1):
        if s[i] == '1':
            print(base, i + 2)
            base = i + 2
        else:
            print(base, i + 2)
