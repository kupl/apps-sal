t = int(input())
while t > 0:
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    m = list()
    m.append(abs(l[0] - l[1]))
    m.append(abs(l[-1] - l[-2]))
    for i in range(1, n - 1, 1):
        if abs(l[i] - l[i - 1]) < abs(l[i] - l[i + 1]):
            m.append(abs(l[i] - l[i - 1]))
        else:
            m.append(abs(l[i] - l[i + 1]))
    print(max(m))
    t -= 1
