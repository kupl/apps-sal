def gap( g, m, n ):
    import math

    np = None
    for i in range( m, n ):
        is_np, e = True, 2
        while e <= math.sqrt( i ) and is_np:
            if i%e == 0:
                is_np = False
            e += 1
        
        if not is_np: 
            continue
        elif np and i - np == g:
            return [np, i]
        else: np = i

    return None
