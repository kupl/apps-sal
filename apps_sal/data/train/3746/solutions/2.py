def next_pal(val):
    val += 1
    while str(val) != str(val)[::-1]:
        val += 1
    return val
