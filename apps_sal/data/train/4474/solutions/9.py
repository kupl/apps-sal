def start_smoking(bars,boxes):
    c=(bars*10+boxes)*18
    r=0
    stub=0
    while(c>0):
        r+=c
        stub+=c
        c,stub=divmod(stub,5)
    return r
