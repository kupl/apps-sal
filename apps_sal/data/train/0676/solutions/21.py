try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        names = list(input().split())
        f = set(names)
        dict = {i: 0 for i in f}
        for i in names:
            dict[i] += 1
        name = min([i for i in names if dict[i] == max(dict.values())])
        print(name)
except Exception:
    pass
