def expanded_form(num):
    parts = str(num).split('.')
    return ' + '.join( [str(int(p) * 10**(len(parts[0])-i-1)) for i,p in enumerate(parts[0]) if p != '0']
                     + ["{}/{}".format(d, 10**i) for i,d in enumerate(parts[1], 1) if d != '0'] )
