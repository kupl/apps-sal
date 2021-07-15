def animals(heads, legs):
    for i in range(heads+1):
        x = heads - i
        if 2 * i + 4 * x == legs :
            return (i, x)
    return 'No solutions'
