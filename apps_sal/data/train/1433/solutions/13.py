tests = int(input())
for t in range(tests):
    a = input()
    b = input()
    aSev = a.count('7')
    aLesS = a.count('5') + a.count('6')
    aFor = a.count('4')
    aLess = a.count('3') + a.count('2') + a.count('1') + a.count('0')
    bSev = b.count('7')
    bLesS = b.count('5') + b.count('6')
    bFor = b.count('4')
    bLess = b.count('3') + b.count('2') + b.count('1') + b.count('0')
    fin7 = 0
    fin4 = 0
    if aSev <= bLesS:
        fin7 += aSev
        bLesS -= aSev
        aSev = 0
    else:
        fin7 += bLesS
        aSev -= bLesS
        bLesS = 0
        if aSev <= bLess:
            fin7 += aSev
            bLess -= aSev
            aSev = 0
        else:
            fin7 += bLess
            aSev -= bLess
            bLess = 0
            if aSev <= bFor:
                fin7 += aSev
                bFor -= aSev
                aSev = 0
            else:
                fin7 += bFor
                aSev -= bFor
                bFor = 0
    if bSev <= aLesS:
        fin7 += bSev
        aLesS -= bSev
        bSev = 0
    else:
        fin7 += aLesS
        bSev -= aLesS
        aLesS = 0
        if bSev <= aLess:
            fin7 += bSev
            aLess -= bSev
            bSev = 0
        else:
            fin7 += aLess
            bSev -= aLess
            aLess = 0
            if bSev <= aFor:
                fin7 += bSev
                aFor -= bSev
                aSev = 0
            else:
                fin7 += aFor
                bSev -= aFor
                aFor = 0
    fin7 += min(aSev, bSev)
    if aFor <= bLess:
        fin4 += aFor
        bLess -= aFor
        aFor = 0
    else:
        fin4 += bLess
        aFor -= bLess
        bLess = 0
    if bFor <= aLess:
        fin4 += bFor
        aLess -= bFor
        bFor = 0
    else:
        fin4 += aLess
        bFor -= aLess
        aLess = 0
    fin4 += min(aFor, bFor)
    print('7' * fin7 + '4' * fin4)
