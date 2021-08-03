def fact(a):
    if(a == 1 or a == 0):
        return 1
    else:
        return a * fact(a - 1)


t = int(input())
for i in range(t):
    a = int(input())
    ans = fact(a)
    print(ans)
