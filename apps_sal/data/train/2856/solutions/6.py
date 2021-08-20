def gap(num):
    return len(max(bin(num)[2:].rstrip('0').split('1')))
