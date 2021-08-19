for t in range(int(input())):
    s = input()
    l = sorted([char for char in s])
    i = 0
    x = []
    cnt = 1
    while i < len(l) - 1:
        if l[i] != l[i + 1]:
            x.append(cnt)
            cnt = 0
        cnt = cnt + 1
        i = i + 1
    x.append(cnt)
    k = len(x)
    while sum(x) % k != 0:
        k = k + 1
    m = sum(x) // k
    z = [max(0, a - m) for a in x]
    for i in range(len(x), 0, -1):
        if sum(x) % i == 0:
            m = sum(x) // i
            break
    y = [max(0, m - a) for a in x]
    print(min(sum(sorted(z)), sum(sorted(y)[0:i])))
