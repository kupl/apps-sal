def gimme(i):
    for x in i:
      if x!=max(i) and x!=min(i):
        return i.index(x)

