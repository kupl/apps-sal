def meeting_time(Ta, Tb, r):
    print(Ta, Tb, r)
    
    if Ta == Tb == 0.00:
        return '{:.2f}'.format(0.00)
    
    pi = 3.14
    len = 2 * pi * r
    if Ta != 0:
        sa = len / Ta
    else:
        sa = 0.00
    if Tb != 0:
        sb = len / Tb
    else:
        sb = 0.00
#     len = sa * T + sb * T
#     len = sa * T - sb * T
    
    if Ta == -Tb:
        return '{:.2f}'.format(abs(float(len / (sa + sb))))
    else:
        return '{:.2f}'.format(abs(float(len / (sa - sb))))
