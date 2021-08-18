def animals(heads, legs):
    return "No solutions" if legs % 2 != 0 or legs < 0 or heads < 0 or legs < 2 * heads or heads < legs / 4 else((heads - ((legs - 2 * heads) / 2), (legs - 2 * heads) / 2))
