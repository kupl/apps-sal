def animals(heads, legs):
    c = (legs - 2 * heads) // 2
    if c < 0 or heads - c < 0 or c * 4 + (heads - c) * 2 != legs:
        return "No solutions"
    else:
        return (heads - c, c)
