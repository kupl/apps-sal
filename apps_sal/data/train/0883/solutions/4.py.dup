for _ in range(int(input())):
    n = int(input())
    l = [int(i) for i in input().split()]
    if n == 1:
        print(-1)
        continue
    if len(set(l)) == 1:
        if l[0] == 0:
            print(n)
        elif l[0] == n - 1:
            print(0)
        else:
            print(-1)
        continue
    if len(set(l)) > 2 or max(l) - min(l) > 1:
        print(-1)
        continue
    # print(l.count(max(l)))
    a = l.count(min(l))
    b = l.count(max(l))
    if max(l) == a:
        print(b)
    else:
        print(-1)
