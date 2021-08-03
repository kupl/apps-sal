try:
    r, c, n = list(map(int, input().split()))
    grid = [[0 for j in range(c)]for i in range(r)]
    for i in range(n):
        a, b = list(map(int, input().split()))
        grid[a][b] = 1
    sumcol = [sum(x) for x in zip(*grid)]
    sumrow = []
    for i in grid:
        sumrow.append(sum(i))

    # targets=[]
    # for i in range(r):
     #   for j in range(c):
      #      targets.append(sumrow[i] + sumcol[j] - 2*grid[i][j])
    print(max(sumrow) + max(sumcol))
except EOFError:
    pass
