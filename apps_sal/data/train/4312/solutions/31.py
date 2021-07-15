def pick_peaks(a):
    po, pe = 'pos', 'peaks'
    d = { po: [], pe: [] }
    for n in range(2, len(a)):
        b, P, e = n-2, n-1, n                              
        if a[ b ] < a[ P ] >= a[ e ]:                           
            if len(a[ P :  ]) != a[ P :  ].count(a[ P ]):    
                if max( a[ P : ] ) >= a[ P ]  :
                    if d[po]:
                        if min( a[ d[po][-1] : P ] ) >= d[pe][-1]:
                            d[po] = d[po][ : -1]
                            d[pe] = d[pe][ : -1]
                    d[po].append( P )
                    d[pe].append( a[ P ] )
    return d
