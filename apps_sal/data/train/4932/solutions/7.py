def flip_row(puzzle, i):
    puzzle[i] = list(map(lambda cell: abs(cell - 1), puzzle[i]))

def flip_col(puzzle, i):
    for row in puzzle:
        row[i] = abs(row[i] - 1)

def find_solution(puzzle):
    result = []
    n = len(puzzle)
    
    for i in range(1,n):
        if puzzle[i] != puzzle[i-1]:
            flip_row(puzzle, i)
            result.append(i)

    for i in range(n):
        if puzzle[0][i] != 1:
            flip_col(puzzle, i)
            result.append(i+n)

    return result
