def arr(n=0): 
    solution = []
    x = -1
    if n == 0:
        return []
    else:
        while len(solution) < n:
            x += 1
            solution.append(x)
    return solution

