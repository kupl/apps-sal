def animals(heads, legs):
    (ch, co) = (2 * heads - legs / 2, legs / 2 - heads)
    return (0, 0) if heads == 0 and legs == 0 else (ch, co) if ch == int(ch) and co == int(co) and (ch >= 0) and (co >= 0) else 'No solutions'
