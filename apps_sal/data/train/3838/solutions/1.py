def goto(l,b):
    if b in ('0','1','2','3') and l in (0,1,2,3):
        return int(b)-l
    return 0
