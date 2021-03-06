ELEMENTS = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']


def get_electron_configuration(element):
    n = ELEMENTS.index(element) + 1
    import re
    a = 'Cr -> ...3d5 4s1 Cu -> ...3d10 4s1 Nb -> ...4d4 5s1 Mo -> ...4d5 5s1 Ru -> ...4d7 5s1 Rh -> ...4d8 5s1 Pd -> ...4d10 5s0 Ag -> ...4d10 5s1 La -> ...4f0 5d1 Ce -> ...4f1 5d1 Gd -> ...4f7 5d1 6s2 Pt -> ...4f14 5d9 6s1 Au -> ...4f14 5d10 6s1 Ac -> ...5f0 6d1 7s2 Th -> ...5f0 6d2 7s2 Pa -> ...5f2 6d1 7s2 U  -> ...5f3 6d1 7s2 Np -> ...5f4 6d1 7s2 Cm -> ...5f7 6d1 7s2'
    a = 'Ni 3d8 4s2 Cr 3d5 4s1 Cu 3d10 4s1 Nb 4d4 5s1 Mo 4d5 5s1 Ru 4d7 5s1 Rh 4d8 5s1 Pd 4d10 5s0 Ag 4d10 5s1 La 4f0 5d1 Ce 4f1 5d1 Gd 4f7 5d1 6s2 Pt 4f14 5d9 6s1 Au 4f14 5d10 6s1 Ac 5f0 6d1 7s2 Th 5f0 6d2 7s2 Pa 5f2 6d1 7s2 U  5f3 6d1 7s2 Np 5f4 6d1 7s2 Cm 5f7 6d1 7s2'
    a = {'Ni': ['Ni', '3d8', '4s2'], 'Ac': ['Ac', '5f0', '6d1', '7s2'], 'Pa': ['Pa', '5f2', '6d1', '7s2'], 'Pt': ['Pt', '4f14', '5d9', '6s1'], 'Ag': ['Ag', '4d10', '5s1'], 'Ru': ['Ru', '4d7', '5s1'], 'Nb': ['Nb', '4d4', '5s1'], 'La': ['La', '4f0', '5d1'], 'U': ['U', '5f3', '6d1', '7s2'], 'Ce': ['Ce', '4f1', '5d1'], 'Th': ['Th', '5f0', '6d2', '7s2'], 'Gd': ['Gd', '4f7', '5d1', '6s2'], 'Au': ['Au', '4f14', '5d10', '6s1'], 'Cm': ['Cm', '5f7', '6d1', '7s2'], 'Pd': ['Pd', '4d10', '5s0'], 'Np': ['Np', '5f4', '6d1', '7s2'], 'Cr': ['Cr', '3d5', '4s1'], 'Rh': ['Rh', '4d8', '5s1'], 'Mo': ['Mo', '4d5', '5s1'], 'Cu': ['Cu', '3d10', '4s1']}
    a = {'Ni': ['3d8', '4s2'], 'Ac': ['5f0', '6d1', '7s2'], 'Gd': ['4f7', '5d1', '6s2'], 'Ag': ['4d10', '5s1'], 'Pt': ['4f14', '5d9', '6s1'], 'Ru': ['4d7', '5s1'], 'Nb': ['4d4', '5s1'], 'La': ['4f0', '5d1'], 'Ce': ['4f1', '5d1'], 'Cm': ['5f7', '6d1', '7s2'], 'Pa': ['5f2', '6d1', '7s2'], 'U': ['5f3', '6d1', '7s2'], 'Cu': ['3d10', '4s1'], 'Th': ['5f0', '6d2', '7s2'], 'Cr': ['3d5', '4s1'], 'Np': ['5f4', '6d1', '7s2'], 'Au': ['4f14', '5d10', '6s1'], 'Rh': ['4d8', '5s1'], 'Mo': ['4d5', '5s1'], 'Pd': ['4d10', '5s0']}
    a = {'Ni': [['3d', '8'], ['4s', '2']], 'Ac': [['5f', '0'], ['6d', '1'], ['7s', '2']], 'Gd': [['4f', '7'], ['5d', '1'], ['6s', '2']], 'Pt': [['4f', '14'], ['5d', '9'], ['6s', '1']], 'Ag': [['4d', '10'], ['5s', '1']], 'Ru': [['4d', '7'], ['5s', '1']], 'Nb': [['4d', '4'], ['5s', '1']], 'La': [['4f', '0'], ['5d', '1']], 'Ce': [['4f', '1'], ['5d', '1']], 'Cm': [['5f', '7'], ['6d', '1'], ['7s', '2']], 'Pa': [['5f', '2'], ['6d', '1'], ['7s', '2']], 'U': [['5f', '3'], ['6d', '1'], ['7s', '2']], 'Cu': [['3d', '10'], ['4s', '1']], 'Th': [['5f', '0'], ['6d', '2'], ['7s', '2']], 'Np': [['5f', '4'], ['6d', '1'], ['7s', '2']], 'Cr': [['3d', '5'], ['4s', '1']], 'Rh': [['4d', '8'], ['5s', '1']], 'Mo': [['4d', '5'], ['5s', '1']], 'Pd': [['4d', '10'], ['5s', '0']], 'Au': [['4f', '14'], ['5d', '10'], ['6s', '1']]}
    o = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f', '6d', '7p', '8s']
    y = {}
    d = {}
    if element in a:
        a = a[element]
        for i in a:
            d[i[0]] = i[1]
    for i in o:
        if i[1] == 's':
            lim = 2
        if i[1] == 'p':
            lim = 6
        if i[1] == 'd':
            lim = 10
        if i[1] == 'f':
            lim = 14
        if n > lim:
            y[i] = str(lim)
            n = n - lim
            continue
        else:
            y[i] = str(n)
            break
    z = dict(list(y.items()) + list(d.items()))
    l = ['1s', '2s', '2p', '3s', '3p', '3d', '4s', '4p', '4d', '4f', '5s', '5p', '5d', '5f', '6s', '6p', '6d', '7s', '7p', '8s']
    r = ''
    for i in l:
        if i in z.keys():
            r += i + z[i] + ' '
    r = element + ' -> ' + r[::-1][1:][::-1]
    return r
