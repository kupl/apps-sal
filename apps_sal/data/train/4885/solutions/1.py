def find_gatecrashers(p, i):
    return sorted(set(p) - {elt for (j, lst) in i for elt in lst + [j]})
