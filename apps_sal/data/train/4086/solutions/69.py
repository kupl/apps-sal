def first_non_consecutive(l):
    for i,n in enumerate(l[1:]):
        if n!=l[i]+1:
            return n
