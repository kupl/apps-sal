def asterisc_it(n):     
    raw = [i for i in list(str(n)) if i.isalnum()]
    txt = '{}'.format(raw[0])
    for i in range(len(raw))[1:]:
        if int(raw[i])%2 == 0:
            if int(raw[i-1]) % 2 == 0:
                txt += '*'+raw[i]
            else: txt += raw[i]        
        else: txt += raw[i]            
    return txt
