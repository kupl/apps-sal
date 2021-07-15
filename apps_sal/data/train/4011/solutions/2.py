def get_free_urinals(urinals):
    if urinals.count('11'): return -1
    return urinals.replace('10', '1').replace('01', '1').replace('00','0').count('0')
