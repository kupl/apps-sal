def sum_str(a, b):
    return str(eval('int(a)+int(b)')) if a and b else '0' if not a and (not b) else b if not a else a
