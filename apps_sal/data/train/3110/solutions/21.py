def two_decimal_places(n):
    a = str(n)
    x = a.split('.')
    l = x[1]
    t = f'{x[0]}.'
    y = ''
    b = ['5','6','7','8','9']
    w = ['0','1','2','3','4','5','6','7','8']
    if l[1] in w and l[2] in b:
        q = l[1]
        w = int(q)
        w =w+1
        y = str(w)
        t = t + f'{l[0]}' + y
    elif l[1] == '9' and l[2] in b:
        q = l[0]
        w = int(q)
        w =w+1
        y = str(w)
        t = t +  y     
    else:
        t = t + f'{l[0]}' + f'{l[1]}'
    final_num = float (t)
    return(final_num)
