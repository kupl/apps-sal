import collections
verbose = False

def setify(s): return { elt if isinstance(elt, collections.Hashable) else tuple(elt) for elt in s }

def match_arrays(v, r): return len(setify(v) & setify(r))
