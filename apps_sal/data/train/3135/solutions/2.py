def meeting_time(ta, tb, r):
    if ta == 0:
        return "{:.2f}".format(abs(tb))
    if tb == 0:
        return "{:.2f}".format(abs(ta))
    else:
        return "{:.2f}".format(abs(ta * tb / (tb - ta)))
