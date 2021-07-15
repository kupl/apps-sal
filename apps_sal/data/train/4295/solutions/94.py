def balanced_num(number):
    ns = str(number)
    nlen = len(ns)
    nmid = nlen//2
    return ['Not Balanced', 'Balanced'][sum(int(c) for c in ns[:nmid-1+nlen%2]) == sum(int(c) for c in ns[nmid+1:])]

