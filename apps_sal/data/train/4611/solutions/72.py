def animals(heads, legs):
    y = legs - 2 * heads
    if y < 0 or y % 2 == 1:
        return "No solutions"

    y //= 2
    x = 2 * heads - legs // 2
    if x < 0 or legs % 2 == 1:
        return "No solutions"

    return (x, y, )
