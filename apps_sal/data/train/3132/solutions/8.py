def alternate_sort(l):
    new=[]
    neg=[x for x in l if x < 0]
    neg.sort()
    neg=neg[::-1]
    pos=[x for x in l if x >= 0]
    pos.sort()
    while neg or pos:
      if neg:
        new.append(neg.pop(0))
      if pos:
        new.append(pos.pop(0))
    return (new)
