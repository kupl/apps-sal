def animals(heads, legs):
    co = (legs - heads * 2) / 2
    ch = heads - co
    return (ch, co) if co.is_integer() and co >= 0 and ch.is_integer() and (ch >= 0) else 'No solutions'
