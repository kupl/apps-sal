cs={'cw':1,'CW':2,'cat':1,'CAT':2,'dog':1,'DOG':2,'movie':1,'MOVIE':2}

def how_much_coffee(events):
    c=sum(cs.get(e,0) for e in events)
    return 'You need extra sleep' if c>3 else c
