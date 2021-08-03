x = eval(input())
for x in range(0, x):
    ans = 0
    d = input()
    a = 0
    cont = 0
    for i in range(0, len(d)):
        a += len(d) - i
        if d[i] == '7':
            ans += 1 + cont
            cont += 1
        else:
            cont = 0
    ans = a - ans
    print(ans)
