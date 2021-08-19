def aa_percentage(prot, rsd='AILMFWYV'):
    rsd = set(rsd)
    return round(sum((p in rsd for p in prot)) / len(prot) * 100)
