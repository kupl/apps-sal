def animals(heads, legs):
    if legs < 2 * heads or 4 * heads - legs < 0 or legs * heads < 0 or legs % 2:
        return "No solutions"
    return (int((4 * heads - legs) / 2), int((legs - 2 * heads) / 2))
