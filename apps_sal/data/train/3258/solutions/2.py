import re

def transpose(amount, tab):
    
    # get start and end of all frets
    fret_pos = get_all_fret_positions(tab)
    # process each column that contains frets
    pos = 0
    tab_new = ['' for string in tab]
    for fret_start in sorted(fret_pos):
        fret_end = fret_pos[fret_start]
        # get all sub strings from one column
        col = [string[fret_start:fret_end] for string in tab]
        # apply amount to all frets
        col, col_width = apply_amount(col, amount)
        if col == 'Out of frets!':
            return 'Out of frets!'
        # adjust column width
        col = adjust_column_width(col, col_width)
        # add modified column back to tablature
        for i, row in enumerate(col):
            tab_new[i] = tab_new[i] + tab[i][pos:fret_start] + row
        pos = fret_end
        # add the part after the final fret
    for i, row in enumerate(col):
        tab_new[i] = tab_new[i] + tab[i][fret_end:]

    return tab_new

def get_all_fret_positions(tab):
    fret_pos = {}
    for string in tab:
        for match in re.finditer('[0-9]+', string):
            if match.start() in fret_pos.keys():
                if fret_pos[match.start()] < match.end():
                    fret_pos[match.start()] = match.end()
            else:
                fret_pos[match.start()] = match.end()
    return fret_pos

def apply_amount(col, amount):
    col_width = 0
    for i, fret in enumerate(col):
        new_fret = re.search('[0-9]+', fret)
        if new_fret:
            new_fret = int(new_fret.group(0)) + amount
            if new_fret > 22 or new_fret < 0:
                return 'Out of frets!', None
            if len(str(new_fret)) > col_width:
                col_width = len(str(new_fret))
            col[i] = str(new_fret)
    return col, col_width

def adjust_column_width(col, col_width):
    for i, row in enumerate(col):
        if len(row) < col_width:
            col[i] = col[i] + '-' * (col_width - len(row))
        if len(row) > col_width:
            col[i] = col[i][:col_width - len(row)]
    return col


t = transpose(2, [
'e|--------5-7-----7-|-8-----8-2-----2-|-0---------0-----|-----------------|',
'B|-10---5-----5-----|---5-------3-----|---1---1-----1---|-0-1-1-----------|',
'G|----5---------5---|-----5-------2---|-----2---------2-|-0-2-2-----------|',
'D|-12-------6-------|-5-------4-------|-3---------------|-----------------|',
'A|------------------|-----------------|-----------------|-2-0-0---0--/8-7-|',
'E|------------------|-----------------|-----------------|-----------------|'])        

print(t)

"""
t = transpose(-1, [
'e|-----------------|---------------|----------------|------------------|',
'B|-----------------|---------------|----------------|------------------|',
'G|--0---3---5----0-|---3---6-5-----|-0---3---5----3-|---0----(0)-------|',
'D|--0---3---5----0-|---3---6-5-----|-0---3---5----3-|---0----(0)-------|',
'A|-----------------|---------------|----------------|------------------|',
'E|-----------------|---------------|----------------|------------------|'])
t = transpose(+2, [
'e|----------5/6-6-6-5/6-6-6-6-6-6------------------------------------|',
'B|-------6--5/6-6-6-5/6-6-6-6-6-6-9-8-6-6----------------------------|',
'G|---6h7--------------------------------6h7--------------------------|',
'D|-8----------------------------------------8-6--8-8-8-8-8-8-8-8-----|',
'A|-----------------------------------------------8-8-8-8-8-8-8-8-----|',
'E|-------------------------------------------------------------------|'])
print(t)
"""

"""
'e|-----------7/8-8-8-7/8-8-8-8-8-8-----------------------------------------------|',
'B|--------8--7/8-8-8-7/8-8-8-8-8-8-11-10-8-8-------------------------------------|',
'G|----8h9----------------------------------8h9-----------------------------------|',
'D|-10------------------------------------------10-8--10-10-10-10-10-10-10-10-----|',
'A|---------------------------------------------------10-10-10-10-10-10-10-10-----|',
'E|-------------------------------------------------------------------------------|'
"""
