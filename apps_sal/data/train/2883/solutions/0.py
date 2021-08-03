def to_pretty(s):
    if not s:
        return "just now"
    for t, w in (60, "seconds"), (60, "minutes"), (24, "hours"), (7, "days"), (53, "weeks"):
        s, r = divmod(s, t)
        if not s:
            return (r > 1 and str(r) + " " + w or ("a ", "an ")[t == 24] + w[:-1]) + " ago"
