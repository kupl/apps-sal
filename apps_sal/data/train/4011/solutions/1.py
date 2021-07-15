def get_free_urinals(urinals):
    if '11' in urinals: return -1
    if urinals == '0': return 1
    free = 0
    i = 0
    while (i < len(urinals)):
        if i == 0 and urinals[i:i+2] == '00' or i > 0 and urinals[i-1:i+2] == '000' or i == len(urinals) - 1 and urinals[i-1:] == '00':
            free += 1
            i += 2
        else:
            i += 1
    return free
