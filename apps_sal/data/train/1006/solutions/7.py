t = int(input())
while t:
    t = t - 1
    (n, d) = list(map(int, input().split()))
    n = list(map(int, list(str(n))))
    n = n[::-1]
    new = []
    count = 0
    m = d
    for i in range(len(n)):
        if n[i] <= m:
            m = n[i]
            new.append(str(n[i]))
        else:
            count += 1
    new = new[::-1]
    for i in range(count):
        new.append(str(d))
    print(''.join(new))
