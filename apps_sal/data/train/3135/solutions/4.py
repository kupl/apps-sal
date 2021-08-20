def meeting_time(Ta, Tb, r):
    if Ta == 0 or Tb == 0:
        return '{:.2f}'.format(abs(Ta + Tb))
    else:
        return '{:.2f}'.format(abs(Ta * Tb) / abs(Ta - Tb))
