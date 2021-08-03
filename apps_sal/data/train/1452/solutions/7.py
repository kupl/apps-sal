t = int(input())
while t > 0:
    t -= 1
    l = input().split(' ')
    m = int(l[0])
    n = int(l[1])
    k = n + 1
    c = 1
    while k != 1:
        c += 1
        k = n + k
        if k > m:
            k = k - m
    if c == m:
        print("Yes")
    else:
        print("No", c)
