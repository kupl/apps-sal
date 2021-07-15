for _ in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
        continue
    ans = ""
    ctr = 0
    for i in range(n):
        ans = ""
        for j in range(ctr):
            ans+='*'
        for j in range(n - ctr, 0, -1):
            ans += str(j)
        print(ans)
        ctr += 1

