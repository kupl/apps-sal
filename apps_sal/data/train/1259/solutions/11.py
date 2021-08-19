t = int(input())
while t:
    (l, r) = input().split()
    l = int(l)
    r = int(r)
    count = 0
    for i in range(l, r + 1):
        rem = i % 10
        if rem == 2 or rem == 3 or rem == 9:
            count = count + 1
    print(count)
    t = t - 1
