def path_finder(maze):
    matrix = list(map(list, maze.splitlines()))
    n = len(matrix)-1
    lst, lst2, count = [(0,0)], [], 0
    while lst:
        count += 1
        while lst:
            a, b = lst.pop()
            matrix[a][b] = "X"
            for i, j in (a+1,b),(a-1,b),(a,b+1),(a,b-1):
                if 0 <= i <= n and 0 <= j <= n and matrix[i][j] == '.':
                    if i == n and j == n:
                        return count
                    lst2.append((i,j))
        lst, lst2 = list(set(lst2)), []
    return False
