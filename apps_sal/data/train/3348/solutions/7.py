def outed(d, boss):
    return ['Get Out Now!','Nice Work Champ!'][(sum(d.values()) + d[boss])/len(d)>5]

