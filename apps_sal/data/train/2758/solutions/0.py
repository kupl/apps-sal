def decode(number):
    return ', '.join(
        str(int(w, 2)) if i % 2 else
        ''.join( chr(int(w[x:x+3])-4) for x in range(0, len(w), 3) )
        for i, w in enumerate( str(number).strip('98').split('98') )
        )
