for t in range(int(input())):
    r, c = list(map(int, input().split()))
    grid = []
    cpy = []
    for i in range(r):
        grid.append(list(input()))
    change = True
    ans = 0
    while(change):
        cpy = [["" for i in range(c)] for j in range(r)]
        change = False
        for i in range(r):
            for j in range(c):
                for ele in grid[i][j]:
                    if(ele == "D" and i < r - 1):
                        change = True
                        if(grid[i + 1][j] != "#"):
                            cpy[i + 1][j] += "D"
                    elif(ele == "U" and i > 0):
                        change = True
                        if(grid[i - 1][j] != '#'):
                            cpy[i - 1][j] += "U"
                    elif(ele == "R" and j < c - 1):
                        change = True
                        if(grid[i][j + 1] != "#"):
                            cpy[i][j + 1] += "R"
                    elif(ele == "L" and j > 0):
                        change = True
                        if(grid[i][j - 1] != '#'):
                            cpy[i][j - 1] += "L"
                    elif(ele == "#"):
                        cpy[i][j] = "#"
        for i in range(r):
            for j in range(c):
                s = cpy[i][j]
                ans += len(s) * (len(s) - 1) / 2
                grid[i][j] = s
    print(int(ans))
