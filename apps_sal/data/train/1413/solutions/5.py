from math import inf

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    r, c = map(int, input().split())
    grid = [[False] * (m + 2) for __ in range(n + 2)]
    for i in range(n):
        s = input()
        for j, x in enumerate(s): grid[i][j] = x == '1'
    solution = [[[inf, inf, inf] for ___ in range(m)] for __ in range(n)]
    r -= 1
    c -= 1
    solution[r][c][0] = 0
    A=[]
    B=[]
    C=[]
    
    A.append(r)
    B.append(c)
    C.append(0)
    
    while len(A):
        r=A.pop(0)
        c=B.pop(0)
        o=C.pop(0)
        new_sol = 1 + solution[r][c][o]
        if o == 0: 
            if grid[r][c + 1] and grid[r][c + 2] and solution[r][c + 1][1] > new_sol:
                solution[r][c + 1][1] = new_sol
                
                A.append(r)
                B.append(c+1)
                C.append(1)
                
                
            if grid[r + 1][c] and grid[r + 2][c] and solution[r + 1][c][2] > new_sol:
                solution[r + 1][c][2] = new_sol
                A.append(r+1)
                B.append(c)
                C.append(2)
                
                
            if grid[r][c - 2] and grid[r][c - 1] and solution[r][c - 2][1] > new_sol:
                solution[r][c - 2][1] = new_sol
                
                A.append(r)
                B.append(c-2)
                C.append(1)
                
                
            if grid[r - 2][c] and grid[r - 1][c] and solution[r - 2][c][2] > new_sol:
                solution[r - 2][c][2] = new_sol
                
                A.append(r-2)
                B.append(c)
                C.append(2)
                
                
        elif o == 1:
            if grid[r][c + 2] and solution[r][c + 2][0] > new_sol:
                solution[r][c + 2][0] = new_sol
                
                A.append(r)
                B.append(c+2)
                C.append(0)
                
            if grid[r + 1][c] and grid[r + 1][c + 1] and solution[r + 1][c][1] > new_sol:
                solution[r + 1][c][1] = new_sol
               
                A.append(r+1)
                B.append(c)
                C.append(1)
                
            if grid[r][c - 1] and solution[r][c - 1][0] > new_sol:
                solution[r][c - 1][0] = new_sol
                
                A.append(r)
                B.append(c-1)
                C.append(0)
                
            if grid[r - 1][c] and grid[r - 1][c + 1] and solution[r - 1][c][1] > new_sol:
                solution[r - 1][c][1] = new_sol
                
                A.append(r-1)
                B.append(c)
                C.append(1)
                
        else: 
            if grid[r][c + 1] and grid[r + 1][c + 1] and solution[r][c + 1][2] > new_sol:
                solution[r][c + 1][2] = new_sol
               
                A.append(r)
                B.append(c+1)
                C.append(2)
                
            if grid[r + 2][c] and solution[r + 2][c][0] > new_sol:
                solution[r + 2][c][0] = new_sol
                
                A.append(r+2)
                B.append(c)
                C.append(0)
                
            if grid[r][c - 1] and grid[r + 1][c - 1] and solution[r][c - 1][2] > new_sol:
                solution[r][c - 1][2] = new_sol
                
                A.append(r)
                B.append(c-1)
                C.append(2)
                
            if grid[r - 1][c] and solution[r - 1][c][0] > new_sol:
                solution[r - 1][c][0] = new_sol
                
                
                A.append(r-1)
                B.append(c)
                C.append(0)
    
    
    for i in range(n):
        for j in range(m):
            print(solution[i][j][0] if solution[i][j][0] != inf else -1, end=' ')
        print()

        
