def double_every_other(lst):
    return [2*v if i&1 else v for i,v in enumerate(lst)]
