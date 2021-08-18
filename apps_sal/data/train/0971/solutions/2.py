for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    final = []
    x = sorted(l, key=l.count)
    for i in x:
        if i != x[-1]:
            final.append(i)
    print(len(final))
