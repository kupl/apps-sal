def format_duration(seconds):
    if seconds == 0:
        return "now"
    units = ((31536000, "year"),
             (86400, "day"),
             (3600, "hour"),
             (60, "minute"),
             (1, "second"))
    ts, t = [], seconds
    for unit in units:
        u, t = divmod(t, unit[0])
        ts += ["{} {}{}".format(u, unit[1], "s" if u > 1 else "")] if u != 0 else []
    return ", ".join([str(d)for d in ts[:-1]]) + (" and " if len(ts) > 1 else "") + ts[-1]
