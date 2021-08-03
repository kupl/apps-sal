t = eval(input())
for i in range(t):
    n = eval(input())
    rem = []
    while(n > 0):
        r = n % 10
        rem.append(r)
        n = n // 10
    print(rem[-1] + rem[0])
