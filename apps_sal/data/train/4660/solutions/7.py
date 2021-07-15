def can_i_play(now,start,end):
    return now in set(list(range(start,25))+list(range(end)) if end<start else range(start,end))
