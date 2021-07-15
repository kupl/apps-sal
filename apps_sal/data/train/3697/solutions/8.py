def list_depth(l):
  inds = [i for i, v in enumerate(l) if isinstance(v, list)]
  return 1 if len(inds) == 0 else 1 + max(list_depth(l[i]) for i in inds)
