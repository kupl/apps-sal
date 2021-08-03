def get_free_urinals(urinals):
    if '11' in urinals:
        return -1
    us = list(map(int, urinals + '00'))
    free = 0
    for i in range(len(urinals)):
        if us[i] == 0 == us[i - 1] == us[i + 1]:
            us[i] = 1
            free += 1
    return free
