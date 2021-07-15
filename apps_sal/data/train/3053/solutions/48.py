def close_compare(a, b, margin=0):
    l=range(b-margin,b+margin+1)
    if a in l: return 0
    elif a<b: return -1
    else: return 1
