for _ in range(int(input())):
    i = int(input())
    s = list(range(1, i + 1))
    v = list(range(i - 1, 0, -1))
    l = s + v
    print(sum([x * x * x for x in l]))
