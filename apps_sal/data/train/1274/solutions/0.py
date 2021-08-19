for _ in range(int(input().strip())):
    n = int(input().strip())
    lst = []
    for i in range(n):
        lst.append(i + 1)
        lst.append(1)
    for i in range(n):
        print(''.join((str(e) for e in lst)))
        for x in range(n):
            lst[x * 2 + 1] += 1
