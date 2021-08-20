t = eval(input())
for q in range(t):
    n = eval(input())
    a = []
    for i in range(n):
        a.append(input().split())
        s = ''
        for x in range(2, len(a[i])):
            s += ' ' + a[i][x]
        a[i][2] = s
    ans = 'Begin on' + a[n - 1][2] + '\n'
    i = n - 2
    while i > -1:
        if a[i + 1][0] == 'Left':
            ans += 'Right on'
        else:
            ans += 'Left on'
        ans += a[i][2] + '\n'
        i -= 1
    print(ans)
