def animals(heads, legs):
    if legs % 2 == 1 or legs > 4 * heads or legs < 2 * heads:
        return "No solutions"
    return (heads - (legs // 2 - heads), legs // 2 - heads)
