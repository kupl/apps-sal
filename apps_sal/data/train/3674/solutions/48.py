def add_binary(a, b):
    total = a + b
    out_str = ''
    while total > 0:
        if total % 2 == 0:
            out_str = '0' + out_str
        else:
            out_str = '1' + out_str
        total = total // 2
    return out_str
