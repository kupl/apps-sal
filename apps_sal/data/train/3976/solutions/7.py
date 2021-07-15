last = lambda *l: l[-1] if len(l)!=1 or not hasattr(l[0], "__getitem__") else l[0][-1]
