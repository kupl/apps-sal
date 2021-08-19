def animals(heads, legs):
    aus = ((4 * heads - legs) / 2, (legs - 2 * heads) / 2)
    return aus if all((v >= 0 and v.is_integer() for v in aus)) else 'No solutions'
