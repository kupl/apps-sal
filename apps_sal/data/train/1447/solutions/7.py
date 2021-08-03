def check(l):
    c = []
    s = list(set(l))
    for i in s:
        c.append(l.count(i))
    if len(c) == len(set(c)):
        return 1
    return 0


for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = 0
    if check(l) == 0:
        print("NO")
        continue
    for i in range(1, n):
        if l[i] != l[i - 1]:
            s += 1
    if s == len(set(l)) - 1:
        print("YES")
    else:
        print("NO")
