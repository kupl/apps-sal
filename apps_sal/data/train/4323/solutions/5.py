def uniq(seq): 
    result = []
    for q in seq:
        if result and result[-1] == q:
            continue
        result.append(q)
    return result
