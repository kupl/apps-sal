def time_correct(t):
    if not t: return t
    time = t.split(":")
    if len(time) != 3 or len(t) != 8: return None
    try:
        time[0] = int(time[0])
    except:
        return None
    try:
        time[1] = int(time[1])
    except:
        return None
    try:
        time[2] = int(time[2])
    except:
        return None
    return "{:02d}:{:02d}:{:02d}".format((time[0]+(time[1]+time[2]//60)//60)%24,(time[1]+time[2]//60)%60,time[2]%60)
