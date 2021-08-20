def animals(heads, legs):
    result = ((heads * 4 - legs) / 2, heads - (heads * 4 - legs) / 2)
    if heads < 0 or legs < 0 or legs % 2 or (min(result) < 0):
        return 'No solutions'
    return result
