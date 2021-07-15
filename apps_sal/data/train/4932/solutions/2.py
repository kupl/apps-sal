def find_solution(puzzle):
    n, sol = len(puzzle), []
    for i in range(n):
        if puzzle[i][0] ^ 1:
            sol.append(i)
    for i in range(1, n):
        if puzzle[0][i] ^ 1 ^ (sol and sol[0] == 0):
            sol.append(n + i)
    return sol
