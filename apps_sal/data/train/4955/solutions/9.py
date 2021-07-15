def ride(group,comet):
    g_c = 1
    c_c = 1
    for a in group:
        g_c*= ord(a)-64
    for a in comet:
        c_c*= ord(a)-64
    
    return "GO" if g_c%47==c_c%47 else "STAY"
