def animals(heads, legs):
    cows = abs((legs - 2 * heads) // 2)
    chicken = abs((4 * heads - legs) // 2)
    return (chicken, cows) if cows + chicken == heads else 'No solutions'
