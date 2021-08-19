def animals(heads, legs):
    for i in range(0, heads + 1):
        for j in range(0, heads + 1):
            if i + j == heads and legs == i * 2 + j * 4:
                return (i, j)
    return 'No solutions'
