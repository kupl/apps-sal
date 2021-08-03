t = eval(input())
while t:
    r = 0
    n = eval(input())
    for i in range(1, n + 1):
        if n % i == 0:
            r = r + 1
    if r % 2 == 1:
        print("YES")
    else:
        print("NO")
    t = t - 1
