import statistics


def count_sec(l):
    return l[0] * 3600 + l[1] * 60 + l[2]


def t(s):
    min, sec = divmod(s, 60)
    hour, min = divmod(min, 60)
    return "|".join([str(int(i)).zfill(2) for i in (hour, min, sec)])


def stat(strg):
    if strg == "":
        return ""
    secs = [count_sec([int(f) for f in i.split("|")]) for i in strg.split(",")]

    h_range = t(max(secs) - min(secs))
    avg = t(statistics.mean(secs))
    med = t(statistics.median(secs))
    return f"Range: {h_range} Average: {avg} Median: {med}"
