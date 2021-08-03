for _ in range(int(input())):
    a = input()
    s = set([])
    for i in range(len(a) - 1):
        s.add(a[i:i + 2])
    print(len(s))
