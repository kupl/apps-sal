n = int(input())
for _ in range(n):
    c, a = [], []
    tot = list(map(int, input().split()))
    done = list(map(int, input().split()))
    for i in range(1, tot[0] + 1):
        if i in done:
            continue
        else:
            if len(c) <= len(a):
                c.append(i)
            else:
                a.append(i)
    c.sort()
    a.sort()
    for j in c:
        print(j, end=" ")
    print()
    for k in a:
        print(k, end=" ")
    print()
