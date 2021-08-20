n = int(input())
for i in range(0, n):
    (r, c) = map(int, input().split())
    if r == 1 and c == 1:
        print(1)
        print(1)
    elif r == 1 and c > 1:
        l = [1, 1, 2, 2]
        if c == 2:
            print(1)
        else:
            print(2)
        for i in range(c):
            print(l[i % 4], end=' ')
        print()
    elif c == 1 and r > 1:
        l = [1, 1, 2, 2]
        if r == 2:
            print(1)
        else:
            print(2)
        for i in range(r):
            print(l[i % 4])
    elif c == 2 and r > 1:
        l = [1, 2, 3]
        if r == 2:
            print(2)
        elif r > 2:
            print(3)
        for i in range(r):
            print(l[i % 3], l[i % 3])
    elif r == 2 and c > 2:
        print(3)
        l = [1, 2, 3]
        for i in range(0, c):
            print(l[i % 3], end=' ')
        print()
        for i in range(0, c):
            print(l[i % 3], end=' ')
        print()
    elif r > 2 and c > 2:
        print(4)
        l = [[1, 1, 3, 3], [2, 2, 4, 4], [3, 3, 1, 1], [4, 4, 2, 2]]
        for i in range(0, r):
            for j in range(0, c):
                print(l[i % 4][j % 4], end=' ')
            print()
