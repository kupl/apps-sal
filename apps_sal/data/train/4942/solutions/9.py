def directions(goal):
    #     print(goal)
    a = {i: goal.count(i) for i in set(goal)}
    print(a)
    b = []
#     print(list(a.keys()) )
    if 'N' in list(a.keys()) and 'S' in list(a.keys()):
        #         print('a.keys()',a.keys())
        if a['N'] > a['S']:
            ns = a['N'] - a['S']
            b.extend(ns * 'N')
        elif a['N'] < a['S']:
            sn = a['S'] - a['N']
            b.extend(sn * 'S')
        elif a['N'] == a['S']:
            sn = a['S'] - a['N']

    elif 'N' in list(a.keys()):
        #         print(a['N'])
        b.extend(a['N'] * str('N'))
    elif 'S' in list(a.keys()):
        #         print(a['S'])
        b.extend(a['S'] * str('S'))
    # Code goes here! :)
    if 'E' in list(a.keys()) and 'W' in list(a.keys()):
        #         print('a.keys()',a.keys())
        if a['E'] > a['W']:
            ew = a['E'] - a['W']
            print(('ew', ew))
            b.extend(ew * str('E'))
        elif a['E'] < a['W']:
            we = a['W'] - a['E']
            print(('we', we))
            b.extend(we * str('W'))
    elif 'W' in list(a.keys()):
        print((a['W']))
        b.extend(a['W'] * str('W'))
    elif 'E' in list(a.keys()):
        print((a['E']))
        b.extend(a['E'] * str('E'))
    return b
