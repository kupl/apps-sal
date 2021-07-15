def merge_arrays(a, b):
    joined = a+b
    noDupes = []
    for x in joined:
        if x not in noDupes:
            noDupes.append(x)
    noDupes.sort()
    return noDupes
#---end function

