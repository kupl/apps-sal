def solve_runes(runes):
    massV = []                
    massV_ind = []
    massD1 = []
    massD2 = []                # more lists to the god of lists!!!!!!!!!!!
    massD1_ind = []
    massD2_ind = []
    ex = []
    mat = []

    expr, value = runes.split('=')

    if expr.find('*',1) != -1:
        ind = expr.index('*',1)
        dig_1 = expr[:ind]
        dig_2 = expr[ind+1:]
        sign = '*'
    elif expr.find('+',1) != -1:
        ind = expr.index('+',1)
        dig_1 = expr[:ind]
        dig_2 = expr[ind+1:]
        sign = '+'
    else:
        ind = expr.index('-',1)
        dig_1 = expr[:ind]
        dig_2 = expr[ind+1:]
        sign = '-'



    for i in range(len(value)):
        if value[i] == "?":
            massV_ind.append(value.index(value[i],i))
            massV.append('0')
        else:
            massV.append(value[i])

    for i in range(len(dig_1)):
        if dig_1[i] == "?":
            massD1_ind.append(dig_1.index(dig_1[i],i))
            massD1.append('0')
        else:
            massD1.append(dig_1[i])
    
    for i in range(len(dig_2)):
        if dig_2[i] == "?":
            massD2_ind.append(dig_2.index(dig_2[i],i))
            massD2.append('0')
        else:
            massD2.append(dig_2[i])

    for i in range(0,10):
        for q in range(len(massD1_ind)):
            massD1[massD1_ind[q]] = str(i)
        for w in range(len(massD2_ind)):
            massD2[massD2_ind[w]] = str(i)
        for e in range(len(massV_ind)):
            massV[massV_ind[e]] = str(i)

        d1 = int(''.join(massD1))
        d2 = int(''.join(massD2))
        val = int(''.join(massV))

        if sign == '*':
            if d1 * d2 == val:
                ex.append(i)

        if sign == '-':
            if d1 - d2 == val:
                ex.append(i)

        if sign == '+':
            if d1 + d2 == val:
                ex.append(i)

                                                # hate
    if dig_1[0] == '-':
        if 1 in massD1_ind:
            if len(massD1)>1:                 
                if 0 in ex:
                    ex.remove(0)
    else:
        if 0 in massD1_ind:
            if len(massD1)>1:
                if 0 in ex:
                    ex.remove(0)
                                                # minuses                    
    if dig_2[0] == '-':
        if 1 in massD2_ind:
            if len(massD2)>1:               
                if 0 in ex:
                    ex.remove(0)
    else:
        if 0 in massD2_ind:
            if len(massD2)>1:
                if 0 in ex:
                    ex.remove(0)

    if value[0] == '-':
        if 1 in massV_ind:
            if len(massV)>1:
                if 0 in ex:
                    ex.remove(0)
    else:
        if 0 in massV_ind:
            if len(massV)>1:
                if 0 in ex:
                    ex.remove(0)


    for i in runes:
        if i in '1234567890':
            mat.append(int(i))
    mat = set(mat)

    if len(ex) == 0:
        return -1
    else:
        for i in ex:
            if i in mat:
                continue
            else:                         # rofl-master
                return i                  # 3 hours
    return -1                             # ------   o,o   -------    -_-
