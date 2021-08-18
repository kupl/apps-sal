import sys
f = sys.stdin
t = int(f.readline())
for r in range(t):
    n, m = map(int, f.readline().rstrip().split())
    if n == 1 and m == 1:
        print("1")
        print("1")
    elif n == 2 and m == 2:
        print("2")
        print("1 2")
        print("1 2")
    elif n == 2 and m == 1:
        print("1")
        print("1")
        print("1")
    elif n == 1 and m == 2:
        print("1")
        print("1 1")
    elif n == 1 and m > 2:
        print("2")
        for i in range(1, m + 1):
            if (i % 4 == 1 or i % 4 == 2):
                print("1", end=" ")
            else:
                print("2", end=" ")
    elif n > 2 and m == 1:
        print("\n2")
        for i in range(1, n + 1):
            if (i % 4 == 1 or i % 4 == 2):
                print("1")
            else:
                print("2")
    elif n == 2 and m > 2:
        print("3")
        for i in range(0, n):
            for j in range(1, m + 1):
                if j % 3 == 1:
                    print("1", end=" ")
                elif j % 3 == 2:
                    print("2", end=" ")
                else:
                    print("3", end=" ")
            print()
    elif n > 2 and m == 2:
        print("3")
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if i % 3 == 1:
                    print("1", end=" ")
                elif i % 3 == 2:
                    print("2", end=" ")
                else:
                    print("3", end=" ")
            print()
    else:
        print("4")
        l = [[0 for x in range(m)] for x in range(n)]
        for q in range(0, m):
            if (q + 1) % 4 != 0:
                l[0][q] = (q + 1) % 4
                l[1][q] = (q + 1) % 4
            else:
                l[0][q] = 4
                l[1][q] = 4
        for i in range(2, n):
            for j in range(1, m - 1):
                l[i][j] = 10 - (l[i - 1][j - 1] + l[i - 2][j] + l[i - 1][j + 1])
            if(l[i][1] != 1):
                l[i][0] = l[i][1] - 1
            else:
                l[i][0] = 4
            if(l[i][m - 2] != 4):
                l[i][m - 1] = l[i][m - 2] + 1
            else:
                l[i][m - 1] = 1
        for i in range(0, n):
            for j in range(0, m):
                print(l[i][j], end=" ")
            print()
