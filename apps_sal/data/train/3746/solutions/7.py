def next_pal(val):
    ret = val + 1
    while str(ret) != str(ret)[::-1]:
        ret += 1
    return ret
