def sect_sort(*args):
    if len(args)==2:
        lst, start=args
        res=lst[:start]+sorted(lst[start:])
    else:
        lst, start, size=args
        if size==0:
            res=lst[:start]+sorted(lst[start:])
        else:
            res=lst[:start]+sorted(lst[start:start+size])+lst[start+size:]
    return res
