def alan(arr):
    a = ['Rejection','Disappointment','Backstabbing Central','Shattered Dreams Parkway']
    s = 0
    r = 0
    d = 0
    b = 0
    sd = 0
    for x in arr:
        for y in a:
            if x == y:
                s += 1
                if y == 'Rejection':
                    r += 1
                elif y == 'Disappointment':
                    d += 1
                elif y == 'Backstabbing Central':
                    b += 1
                else:
                    sd += 1
    if s >= 4 and r>0 and d>0 and b>0 and sd>0:
        return 'Smell my cheese you mother!'
    else:
        return 'No, seriously, run. You will miss it.'

