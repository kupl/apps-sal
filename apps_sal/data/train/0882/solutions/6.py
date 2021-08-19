# cook your dish here
t = int(input())
while t > 0:
    a = input()
    b = input()
    ans = 0
    for i in a:
        if i in b:
            ans += 1
            b = b.replace(i, '', 1)
    print(ans)
    t -= 1
