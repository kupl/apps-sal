PTS  = {'kata':5, 'Petes kata':10, 'life':0, 'eating':1}
OUTS = ((100,'Miserable!'), (70,'Sad!'), (40,'Happy!'), (0,'Super happy!'))

def paul(lst):
    v = sum(map(PTS.__getitem__, lst))
    return next(s for limit,s in OUTS if v>=limit)
