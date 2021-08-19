def find_solution(puzzle):
    first_column = [i for i in range(len(puzzle)) if puzzle[i][0] == 0]
    value = 1 if 0 in first_column else 0
    first_row = [i + len(puzzle) for i in range(len(puzzle)) if puzzle[0][i] == value]
    return first_row + first_column
