def interleave(*args):
    arr = []
    for i in range(max((len(a) for a in args))):
        for j in range(len(args)):
            try:
                arr.append(args[j][i])
            except:
                arr.append(None)
    return arr
