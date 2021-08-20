def meeting_time(Ta, Tb, r):
    if Ta == 0 and Tb == 0:
        return '0.00'
    if Ta == 0:
        return '%.2f' % abs(Tb)
    if Tb == 0:
        return '%.2f' % abs(Ta)
    if Ta > 0 and Tb > 0 or (Ta < 0 and Tb < 0):
        return '%.2f' % (Ta * Tb / abs(abs(Ta) - abs(Tb)))
    if Ta > 0 and Tb < 0 or (Tb > 0 and Ta < 0):
        return '%.2f' % (abs(Ta * Tb) / abs(abs(Ta) + abs(Tb)))
