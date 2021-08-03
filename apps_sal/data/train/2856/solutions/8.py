def gap(num):
    return max(len(seq) for seq in format(num, 'b').strip('0').split('1'))
