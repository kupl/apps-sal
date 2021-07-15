def black_or_white_key(keycount):
    black=2,5,7,10,12
    x=keycount%88
    if x==0:
        return "white"
    else: 
        if x%12 in black or x%12==0:
            return "black"
        else:
            return "white"
