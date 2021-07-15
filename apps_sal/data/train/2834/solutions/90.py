def symmetric_point(p, q):
    x1=int(str(p).split(',')[0].split('[')[1])
    y1=int(str(p).split(',')[1].split(']')[0])
    x2=int(str(q).split(',')[0].split('[')[1])
    y2=int(str(q).split(',')[1].split(']')[0])
    
    return [x2+(x2-x1), y2+(y2-y1)]
