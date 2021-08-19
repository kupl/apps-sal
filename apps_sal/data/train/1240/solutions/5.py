for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    s = 0
    for i in l:
        if i % 6 == 0:
            s += 6
        else:
            s += i % 6
    print(s)
