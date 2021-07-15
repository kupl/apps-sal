def remove_duplicate_words(s):
    res = {}
    for i,n in enumerate(s.split()):
        if n not in res:
            res[n] = i
    
    return ' '.join(sorted(res, key=res.get))
