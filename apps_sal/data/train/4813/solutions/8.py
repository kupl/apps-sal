def get_num(n):
    n = str(n).replace('8', '00').replace('9', '0').replace('6', '0')
    return n.count('0')
