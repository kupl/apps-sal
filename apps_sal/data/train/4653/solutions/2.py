from string import ascii_lowercase as aLow

tr = aLow[1:]+'a'
TABLE = str.maketrans(aLow+aLow.upper(), tr+tr.upper())

def next_letter(s): return s.translate(TABLE)
