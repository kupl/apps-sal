t = int(input())
while(t):
    t -= 1
    a = input()
    n = len(a)
    inds = [-1]
    for i in range(n):
        if(a[i] == 'R'):
            inds.append(i)
    inds.append(n)
    ans = 0
    for i in range(1, len(inds)):
        ans = max(ans, inds[i] - inds[i - 1])
    print(ans)
