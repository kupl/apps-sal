def seven_generator(m):
    if m < 100:
        return
    x, y = divmod(m, 10)
    nxt = x - 2*y
    yield nxt
    yield from seven_generator(nxt)
        
        
def seven(m):
    l = list(seven_generator(m))
    return (l[-1] if l else 0, len(l))
        

