def solve(arr):
    solution = []
    for i in reversed(arr):
        if i not in solution:
            solution.append(i)
    solution.reverse()
    return solution
