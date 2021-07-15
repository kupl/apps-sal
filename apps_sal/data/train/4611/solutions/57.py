def animals(heads, legs):
    if (heads < 0) or (legs < 0) or (heads > 1000) or (legs % 2 == 1):
        return "No solutions" 
    else:
        x = (4 * heads - legs) /2
        y = heads - x
        if x < 0 or y < 0:
            return "No solutions"
        else:
            return (x, y)
