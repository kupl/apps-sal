def check(seq, elem):
    result=False
    for n in seq:
        if n==elem:
            result=True
            break
        else: continue
    return result
