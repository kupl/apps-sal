def myKey(l):
    return -l[1]


t = int(input())
for tests in range(t):
    n = int(input())
    ca = []
    for i in range(n):
        l = input()
        l = l.split()
        l[0] = int(l[0])
        l[1] = int(l[1])
        ca.append(l)
    if n == 1 and ca[0][1] == 0:
        print('0')
        continue
    ca.sort(key=myKey)
    for i in range(n):
        ca[i][0] *= ca[i][1]
        ca[i][1] -= 1
    ans = ''
    for i in range(n - 1):
        if ca[i][0] != 0:
            if ca[i][1] != 0:
                ans += str(ca[i][0]) + 'x^' + str(ca[i][1]) + ' + '
            else:
                ans += str(ca[i][0]) + ' + '
    if ca[n - 1][0] != 0:
        if ca[n - 1][1] != 0:
            ans += str(ca[n - 1][0]) + 'x^' + str(ca[n - 1][1])
        else:
            ans += str(ca[n - 1][0])
    else:
        ans = ans[:-3]
    print(ans)
