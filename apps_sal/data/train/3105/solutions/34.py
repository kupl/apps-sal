def count_sheep(n):
    opstr = 'sheep...'
    
    oplst = []
    
    count = 1
    while count <= n:
        oplst.append(str(count) + ' ' + opstr)
        count += 1
    
    return ''.join(oplst)
