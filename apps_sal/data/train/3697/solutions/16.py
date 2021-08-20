def list_depth(L):
    try:
        return 1 + max((list_depth(e) for e in L if isinstance(e, list)))
    except:
        return 1
