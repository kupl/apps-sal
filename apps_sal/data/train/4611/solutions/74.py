def animals(heads, legs):
    x = ((heads * 4) - legs) / 2
    return (int(x), int(heads - x)) if legs >= heads and x >= 0 and int(x) == x else 'No solutions'
