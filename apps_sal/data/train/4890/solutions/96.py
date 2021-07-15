def find_difference(a, b):
    
    vola=a[0]*a[1]*a[2]
    volb=b[0]*b[1]*b[2]
    
    if vola > volb:
        diff=vola-volb
        return diff
    if volb > vola:
        diff=volb-vola
        return diff
    if vola-volb or volb-vola == 0:
        return 0
