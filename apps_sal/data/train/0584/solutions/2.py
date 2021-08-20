t = int(input())
for x in range(t):
    a = list(input())
    N = len(a)
    i = 0
    for i in range(i + 1, N):
        if a[i - 1] == '0' and a[i] == '1':
            a = a[:i]
            break
    if '1' in a:
        print(a.count('0'))
    else:
        print(0)
