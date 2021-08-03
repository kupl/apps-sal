def tiaosheng(failed_counter):
    n = 60
    for c in failed_counter:
        if c <= n:
            n -= min(3, n - c)
    return n
