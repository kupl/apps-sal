def champernowneDigit(n):
    if not n or type(n)!=int or n<0: return float('nan')
    if n<=10: return n-1
    digs=1
    tot=1
    while 1:
        if tot+digs*9*10**(digs-1)>=n: break
        tot+=digs*9*10**(digs-1)
        digs+=1
    number=(n-tot-1)//digs+10**(digs-1)
    return int(str(number)[(n-tot-1)%digs])
