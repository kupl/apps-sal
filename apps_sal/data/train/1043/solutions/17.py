t = int(input())
ans1 = list()
for i in range(t):
    n = list(map(int, input().split()))
    s = list(map(str, input().split()))
    ans = list()
    for j in range(n[1]):
        a = list(map(str, input().split()))
        ans.append(a)
    d = list()
    for j in ans:
        d = d + j
    yo = ''
    for k in range(len(s)):
        if s[k] in d:
            yo = yo + 'YES' + ' '
        else:
            yo = yo + 'NO' + ' '
    ans1.append(yo)
for l in ans1:
    print(l)
