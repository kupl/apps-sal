def meeting_time(Ta, Tb, r):
    if Ta == Tb:
        return "0.00"
    if Ta == 0:
        return "{:.2f}".format(abs(Tb))
    if Tb == 0:
        return "{:.2f}".format(abs(Ta))
    return "{:.2f}".format(abs(Ta * Tb) / abs(Ta - Tb), 2)
