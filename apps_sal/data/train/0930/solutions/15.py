for _ in range(int(input())):
    n = int(input())
    x = 1
    y = n
    a = [[0 for i in range(n)] for j in range(n)]
    for (indx1, i) in enumerate(a):
        if indx1 == 0:
            for (indx2, j) in enumerate(i):
                if indx2 == 0:
                    a[indx1][indx2] = 1
                else:
                    a[indx1][indx2] = a[indx1][indx2 - 1] + x
                    x += 1
        else:
            for (indx2, j) in enumerate(i):
                if indx2 == n - 1:
                    a[indx1][indx2] = a[indx1 - 1][indx2] + y
                    y -= 1
                else:
                    a[indx1][indx2] = a[indx1 - 1][indx2 + 1] + 1
    for i in a:
        for j in i:
            print(j, end=' ')
        print()
