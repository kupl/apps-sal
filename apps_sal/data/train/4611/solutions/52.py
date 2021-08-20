def animals(heads, legs):
    (ch, co) = ((4 * heads - legs) / 2, (legs - 2 * heads) / 2)
    if ch < 0 or co < 0 or int(ch) != ch or (int(co) != co):
        return 'No solutions'
    return (ch, co)
