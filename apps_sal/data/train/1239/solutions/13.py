for _ in range(int(input())):
    k = int(input())
    ans = [str(k)]
    s = str(k)
    n = k
    while n > 0:
        n -= 1
        s = s + str(n)
        ans.append(s)
    ans = ans + ans[:-1][::-1]
    for x in ans:
        z = ' ' * (k + 1 - len(x))
        print(z + x)
