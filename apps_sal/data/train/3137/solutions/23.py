def round_it(n):
    dec_pos = str(n).find(".")
    num_before = dec_pos
    num_after = (len(str(n)) - dec_pos) - 1
    if num_before < num_after:
        return int(n + 1)
    elif num_before > num_after:
        return int(n)
    elif num_before == num_after:
        return round(n)
    return
