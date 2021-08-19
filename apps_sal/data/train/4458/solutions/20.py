def time_correct(t=None):
    if t == '':
        return ''
    elif t == None or len(t) != 8 or t[2] != ':' or (t[5] != ':'):
        return None
    elif (t[0:2] + t[3:5] + t[6:]).isdigit():
        if int(t[6:]) >= 60:
            ts = str(int(t[6:]) % 60).zfill(2)
            tsp = int(t[6:]) // 60
        else:
            ts = t[6:].zfill(2)
            tsp = 0
        if int(t[3:5]) + tsp >= 60:
            tm = str((int(t[3:5]) + tsp) % 60).zfill(2)
            tmp = (int(t[3:5]) + tsp) // 60
        else:
            tm = str(int(t[3:5]) + tsp).zfill(2)
            tmp = 0
        if int(t[0:2]) + tmp >= 24:
            th = str((int(t[0:2]) + tmp) % 24).zfill(2)
        else:
            th = str(int(t[:2]) + tmp).zfill(2)
        return th + ':' + tm + ':' + ts
    else:
        return None
