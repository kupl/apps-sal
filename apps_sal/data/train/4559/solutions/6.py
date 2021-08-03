def ones_complement(b):
    b = b.replace('0', '*')
    b = b.replace('1', '0')
    return b.replace('*', '1')  # your code here
