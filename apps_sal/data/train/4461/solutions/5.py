def boxes_packing(length, width, height):
    boxes=sorted([sorted(t,reverse=True) for t in zip(length,width,height)],reverse=True)
    for b1,b2 in zip(boxes[:-1],boxes[1:]):
        if b1[0]<=b2[0] or b1[1]<=b2[1] or b1[2]<=b2[2]:
            return False
    return True
