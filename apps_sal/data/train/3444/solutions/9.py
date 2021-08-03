def cyclic_string(s):
    if len(set(s)) == 1:
        return 1
    alist = []
    for i in s:
        alist.append(i)
        if s in "".join(alist) * 15:
            return len(alist)
