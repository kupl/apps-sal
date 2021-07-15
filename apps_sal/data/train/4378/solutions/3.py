def find_spaceship(amap):
    a=amap.split('\n')[::-1]
    for i in a:
        if 'X' in i:
            return[ i.index('X') , a.index(i) ]
    return "Spaceship lost forever."
