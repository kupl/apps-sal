def chameleon(chameleons, color):
    (_,a), (_,b), (_,c) = sorted((i==color, v) for i,v in enumerate(chameleons))
    return -1 if not a and not c or (b-a) % 3 else b
