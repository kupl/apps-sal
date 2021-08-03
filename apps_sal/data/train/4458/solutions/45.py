def time_correct(t):
    try:
        if t == None:
            return t
        if t == "":
            return t
        if len(t) == 8:
            if t.count(":") > 0:
                t = t.split(":")
            if t[0] == "00":
                first = 0
            else:
                first = int(t[0])
            second = int(t[1])
            third = int(t[2])
            if third >= 60:
                third -= 60
                second += 1
            if second >= 60:
                second -= 60
                first += 1
            while first >= 24:
                first -= 24
            return "{}:{}:{}".format(str(first).zfill(2), str(second).zfill(2), str(third).zfill(2))
    except:
        return None
