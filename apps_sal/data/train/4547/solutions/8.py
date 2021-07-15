def zero_dominant(c):
    s = format(ord(c), 'b')
    return s.count('0') > s.count('1')

def more_zeros(s):
    return list(dict.fromkeys(c for c in s if zero_dominant(c)))
