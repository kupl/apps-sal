def bingo(card, numbers):
    card = card[1:]
    c = 'BINGO'
    r =[]
    
    #col
    col = []
    for i,v in enumerate(c):
        for j in range(5):
            s = f'{v}{card[j][i]}'
            if s != 'NFREE SPACE':
                col.append(s)
        r.append(col)
        col = []
            
    #row
    row = []
    for j in range(5):
        for i,v in enumerate(c):
            s = f'{v}{card[j][i]}'
            if s != 'NFREE SPACE':
                row.append(s)
        r.append(row)
        row = []
            
    #down diag
    dd = []
    for i in range(5):
        s = f'{c[i]}{card[i][i]}'
        if s != 'NFREE SPACE':
            dd.append(s)
    r.append(dd)
        
    #up diag
    du = []
    for i in range(4,-1,-1):
        s = f'{c[4-i]}{card[i][4-i]}'
        if s != 'NFREE SPACE':
            du.append(s)
    r.append(du)
    
    for x in r:
        if all(i in numbers for i in x):
            return 1
    return 0
