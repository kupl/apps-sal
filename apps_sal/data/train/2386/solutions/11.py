for t in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))

    s = set()
    l = []
    for i in a:
        if not i in s:
            l.append(i)
            s.add(i)
    print(" ".join(map(str, l)))
