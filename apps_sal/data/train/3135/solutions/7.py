def meeting_time(Ta, Tb, r):
    if Ta == 0:
        if Tb == 0:
            return '0.00'
        else:
            return str(abs(Tb)) + '.00'
    if Tb == 0:
        return str(abs(Ta)) + '.00'
    if Ta == Tb:
        return '0.00'
    Aa = 360 / Ta
    Ab = 360 / Tb
    if Aa > 0 and Ab > 0:
        return str(format(abs(360 / abs(Ab - Aa)), '.2f'))
    elif Aa < 0 and Ab < 0:
        return str(format(abs(360 / abs(Ab - Aa)), '.2f'))
    else:
        return str(format(abs(360 / (abs(Ab) + abs(Aa))), '.2f'))
