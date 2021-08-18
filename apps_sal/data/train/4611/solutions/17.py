
def animals(heads, legs):
    for x in range(heads + 1):
        if 2 * x + 4 * (heads - x) == legs:
            return (x, heads - x)
    return "No solutions"
