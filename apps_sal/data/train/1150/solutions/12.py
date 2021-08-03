t = int(input())
i = 0
while i < t:
    n = int(input())
    j = n
    c = 0
    while n > 0:
        r = int(n**(0.5))
        c += 1
        n = n - r**2
    print(c)
    i += 1
