def animals(heads, legs):
    if heads == 0 and legs == 0:
        return (0, 0)
    elif heads < 0 or legs < 0 or heads > legs or (legs > heads * 4) or legs % 2:
        return 'No solutions'
    else:
        cows = (heads * 4 - legs) // 2
        chickens = heads - (heads * 4 - legs) // 2
        return (cows, chickens) if heads - cows - chickens == 0 else 'No solution'
