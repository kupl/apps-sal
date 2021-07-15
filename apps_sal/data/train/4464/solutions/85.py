def feast(beast, dish):
    bfirst = beast[0]
    blast = beast[-1]
    dfirst = dish[0]
    dlast = dish[-1]
    if bfirst == dfirst and blast == dlast:
        return(True)
    else:
        return(False)
