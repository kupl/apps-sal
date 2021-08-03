def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)


t = int(input())
for u in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = a[0]
    for i in a:
        h = gcd(ans, i)
        if(h > ans):
            ans = h
        else:
            break
    a.reverse()
    ans2 = a[0]
    for i in a:
        h = gcd(ans2, i)
        if(h > ans):
            ans2 = h
        else:
            break
    ans3 = gcd(ans, ans2)
    print(max(ans, max(ans2, ans3)))
