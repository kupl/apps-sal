def meeting_time(Ta, Tb, r):
    if Ta == 0:
        return '{:.2f}'.format(abs(Tb))
    elif Tb == 0:
        return '{:.2f}'.format(abs(Ta))
    else:
        return '{:.2f}'.format(abs(Ta * Tb / (Tb - Ta)))
