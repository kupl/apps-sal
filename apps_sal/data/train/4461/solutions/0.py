def boxes_packing(l, w, h):
    boxes = sorted(sorted(t) for t in zip(l, w, h))
    return all( s < l for b1,b2 in zip(boxes[:-1], boxes[1:]) for s,l in zip(b1,b2))
