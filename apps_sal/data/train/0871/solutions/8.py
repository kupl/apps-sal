for i in range(int(input())):
    (r, c) = [int(a) for a in input().split()]
    a = []
    for i in range(r):
        a.append(input())
    n = max(r, c)
    lst = [0 for i in range(n)]
    complete_list = []
    for i in range(r):
        z = []
        for j in range(c):
            z.append(lst.copy())
        complete_list.append(z)
    for i in range(r):
        for j in range(c):
            if a[i][j] == 'R':
                l = 1
                for p in range(j + 1, c):
                    if a[i][p] == '#':
                        break
                    complete_list[i][p][l] += 1
                    l += 1
            elif a[i][j] == 'L':
                l = 1
                for p in range(j - 1, -1, -1):
                    if a[i][p] == '#':
                        break
                    complete_list[i][p][l] += 1
                    l += 1
            elif a[i][j] == 'D':
                l = 1
                for p in range(i + 1, r):
                    if a[p][j] == '#':
                        break
                    complete_list[p][j][l] += 1
                    l += 1
            elif a[i][j] == 'U':
                l = 1
                for p in range(i - 1, -1, -1):
                    if a[p][j] == '#':
                        break
                    complete_list[p][j][l] += 1
                    l += 1
    ans = 0
    for i in range(r):
        for j in range(c):
            for p in range(n):
                if complete_list[i][j][p] == 2:
                    ans += 1
                elif complete_list[i][j][p] == 3:
                    ans += 3
                elif complete_list[i][j][p] == 4:
                    ans += 6
    print(ans)
