def chmod_calculator(perm):
    oct = ''
    for j in ['user', 'group', 'other']:
        try:
            oct += str(sum([2 ** (2 - i[0]) for i in list(enumerate(perm[j], 0)) if i[1] != '-']))
        except:
            oct += '0'
    return oct
