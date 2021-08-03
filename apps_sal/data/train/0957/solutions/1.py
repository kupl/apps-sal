n = int(input())
for i in range(n):
    p = int(input())
    l = list(map(int, input().split()))
    l.sort()
    minlist = []
    minlist.append(abs(l[0] - l[1]))
    minlist.append(abs(l[len(l) - 1] - l[len(l) - 2]))
    for i in range(1, len(l) - 1):
        r = abs(l[i] - l[i - 1])
        p = abs(l[i] - l[i + 1])
        minlist.append(min(r, p))
    print(max(minlist))
