def time_correct(t):
    if t == "":
        return ""
    if not t or len(t) != 8 or not (t[0:2] + t[3:5] + t[6:8]).isdigit() or not t[2] + t[5] == "::":
        return None
    return "%s:%s:%s" % (str((int(t[0:2]) + ((int(t[3:5]) + (int(t[6:8]) // 60)) // 60)) % 24).zfill(2),
                         str((int(t[3:5]) + (int(t[6:8]) // 60)) % 60).zfill(2), str(int(t[6:8]) % 60).zfill(2))
