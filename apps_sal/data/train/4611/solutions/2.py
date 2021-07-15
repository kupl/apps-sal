def animals(heads, legs):
    solution = (2 * heads - legs/2, legs/2 - heads)
    return solution if legs % 2 == 0 and solution[0] >= 0 and solution[1] >= 0 else "No solutions"
