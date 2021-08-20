def animals(heads, legs):
    if heads < 0 or legs < 0 or legs % 2 != 0:
        return 'No solutions'
    chicken = (4 * heads - legs) // 2
    cows = heads - chicken
    if chicken >= 0 and cows >= 0 and (chicken + cows == heads):
        return (chicken, cows)
    else:
        return 'No solutions'
