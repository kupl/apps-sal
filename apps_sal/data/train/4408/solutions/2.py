def yoga(room, poses):
    return sum(sum(v <= p + s for v in poses for p in r) for r, s in ((r, sum(r)) for r in room))
