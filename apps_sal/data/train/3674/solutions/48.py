def add_binary(a, b):
    # binary is base 2.
    total = a + b
    out_str = ""
    while total > 0:
        if total % 2 == 0:
            out_str = "0" + out_str  # prepend
        else:
            out_str = "1" + out_str
        total = total // 2  # make sure to use integer division
    return out_str
