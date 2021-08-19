for t in range(int(input())):
    c = 0
    for i in range(int(input())):
        (s, j) = [int(x) for x in input().rstrip().split()]
        if j - s > 5:
            c += 1
    print(c)
