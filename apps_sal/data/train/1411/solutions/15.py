# cook your dish here
a = int(input())
for i in range(0, a):
    x, r, a, b = map(int, input().split())
    maxx = max(a, b)
    minn = min(a, b)
    ans = x - x * (minn / maxx)
    if(ans - int(ans) == 0):
        ans = ans - 1
    else:
        ans = int(ans)
    print(int(ans))
