t = int(input())
for i in range(t):
    n = int(input())
    suffixes = {}
    xx = input().split()
    for x in range(n):
        try:
            a = suffixes[xx[x][-3:]]
        except Exception as e:
            a = []
        a.append(xx[x])
        suffixes.update({xx[x][-3:]: a})
    print('Case : %d' % (i + 1))
    for a in sorted(suffixes):
        print(''.join((b + ' ' for b in sorted(suffixes[a]))).strip())
