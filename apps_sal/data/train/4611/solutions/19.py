def animals(heads, legs):
    for x in range(heads + 1):
        if x * 2 + (heads - x) * 4 == legs:
            return (x, heads - x)
    return 'No solutions'
