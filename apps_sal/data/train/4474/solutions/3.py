def start_smoking(bars, boxes):
    new = (bars * 10 + boxes) * 18
    smoked = ends = 0
    
    while new:
        smoked += new
        ends += new
        new = ends // 5
        ends -= new * 5
    
    return smoked
