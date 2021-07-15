def past(h, m, s):
    # 1 h - 3600000 ms
    # 1 m - 60000 ms
    # 1 s - 1000 ms
    return h*3600000+m*60000+s*1000
