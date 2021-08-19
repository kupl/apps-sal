# cook your dish here
for _ in range(int(input())):
    r, c = map(int, input().split())
    a = []
    for i in range(r):
        a.append(list(map(int, input().split())))
    cont = True
    for i in range(r):
        for j in range(c):
            if ((i == 0 and j == c - 1) or (i == r - 1 and j == 0)
                    or (i == r - 1 and j == c - 1) or (i == 0 and j == 0)):
                if a[i][j] > 1:
                    cont = False
                    break
            elif i == 0 or i == r - 1 or j == 0 or j == c - 1:
                if a[i][j] > 2:
                    cont = False
                    break
            else:
                if a[i][j] > 3:
                    cont = False
                    break
        if cont == False:
            print('Unstable')
            break
    else:
        print('Stable')
