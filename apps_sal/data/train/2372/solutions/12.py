t = int(input())
while t:
    t += -1
    ans = 999999999999
    n = int(input())
    s = 1
    while 1:
        tmp = n // s + bool(n % s) - 1 + (s - 1)
        if tmp > ans:
            break
        ans = tmp
        s -= -1
    print(ans)
