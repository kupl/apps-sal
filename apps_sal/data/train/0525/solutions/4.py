# cook your dish here
try:
    t = int(input())
    for i in range(t):
        a, b, c = map(int, input().split())
        x = c // a
        ans = (x * a) + b
        if(ans > c):
            ans = ans - a
        print(ans)

except:
    pass
