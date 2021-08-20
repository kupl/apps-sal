try:
    l = []
    for _ in range(int(input())):
        arr = [int(i) for i in input().split()]
        a = 0
        x = arr.count(1)
        if x >= 2:
            l.append(1)
    ans = sum(l)
    print(ans)
except EOFError as error:
    pass
