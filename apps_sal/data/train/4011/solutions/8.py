def get_free_urinals(urinals):
    count = 0
    urinals = list(urinals)
    for i in range(len(urinals)):
        if urinals[i] == '1' and i + 1 != len(urinals) and (urinals[i + 1] == '1'):
            return -1
        if urinals[i] == '0' and (i == 0 or urinals[i - 1] == '0') and (i + 1 == len(urinals) or urinals[i + 1] == '0'):
            urinals[i] = '2'
    return urinals.count('2')
