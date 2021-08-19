def more_zeros(s):
    return [v for (i, v) in enumerate(s) if bin(ord(v))[2:].count('0') > bin(ord(v))[2:].count('1') and v not in s[:i]]
