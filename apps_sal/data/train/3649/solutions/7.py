def aa_percentage(seq,codes="AILMFWYV"):
    codes=set(codes)
    return round(sum(c in codes for c in seq)/len(seq)*100)

