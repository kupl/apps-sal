def middle_point(*args):
    sortLst = sorted( args[i:i+3] for i in range(0,9,3) )
    return [i for i in range(0,9,3) if args[i:i+3] == sortLst[1]][0]/3 + 1
