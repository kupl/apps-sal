def sum_str(a, b):
    return str(sum([int(a), int(b)]) if len(a) > 0 and len(b) > 0 else a + b if len(a) > 0 or len(b) > 0 else '0')
