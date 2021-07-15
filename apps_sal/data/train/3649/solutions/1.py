def aa_percentage(seq, acid='AILMFWYV'):
    return round(sum(x in acid for x in seq) * 100 / len(seq) )
