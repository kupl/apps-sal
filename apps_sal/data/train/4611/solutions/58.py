def animals(heads, legs):
    # conditions: heads <= 1000 and legs <= 1000
    # IMPORTANT: legs will always be an even number
    # Also: x and y can't be less than zero!

    if (heads < 0) or (legs < 0) or (heads > 1000) or (legs % 2 == 1):
        return "No solutions"
    else:
        x = (4 * heads - legs) / 2
        y = heads - x
        if x < 0 or y < 0:
            return "No solutions"
        else:
            return (x, y)
