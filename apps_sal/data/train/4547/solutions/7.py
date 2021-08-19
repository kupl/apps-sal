def more_zeros(s):
    lst0 = []
    lst1 = []
    lst_res = []
    stage = 0
    while stage != len(s):
        tmp = '{0:b}'.format(ord(s[stage]))
        for x in tmp:
            if x == '1':
                lst1.append(x)
            else:
                lst0.append(x)
        if len(lst1) < len(lst0):
            if s[stage] in lst_res:
                stage = stage + 1
                lst1 = []
                lst0 = []
                pass
            else:
                lst_res.append(s[stage])
                stage = stage + 1
                lst1 = []
                lst0 = []
        else:
            stage = stage + 1
            lst1 = []
            lst0 = []
    return lst_res
