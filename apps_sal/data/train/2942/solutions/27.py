def fold_to(distance):
    paper_thick = 0.0001
    folding=0
    if distance < 0:
        return None
    elif distance == 0:
        return 0
    while distance > paper_thick:
        paper_thick = paper_thick*2
        folding+=1
    return folding

