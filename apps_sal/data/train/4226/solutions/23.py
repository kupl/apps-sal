def remove_smallest(ns):
    nss = ns.copy()
    nss.remove(min(ns)) if nss else None
    return nss
