ELEMENTS = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']


def orbital_sort(s):
    return s.replace('s', '1').replace('p', '2').replace('d', '3').replace('f', '4')


def get_electron_configuration(element):
    atomic = ELEMENTS.index(element) + 1

    filling = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f', '6d', '7p', '8s']

    replace_d = {
        'Cr': '3d5 4s1',
        'Cu': '3d10 4s1',
        'Nb': '4d4 5s1',
        'Mo': '4d5 5s1',
        'Ru': '4d7 5s1',
        'Rh': '4d8 5s1',
        'Pd': '4d10 5s0',
        'Ag': '4d10 5s1',
        'La': '4f0 5s2 5p6 5d1 6s2',
        'Ce': '4f1 5s2 5p6 5d1 6s2',
        'Gd': '4f7 5s2 5p6 5d1 6s2',
        'Pt': '4f14 5s2 5p6 5d9 6s1',
        'Au': '4f14 5s2 5p6 5d10 6s1',
        'Ac': '5f0 6s2 6p6 6d1 7s2',
        'Th': '5f0 6s2 6p6 6d2 7s2',
        'Pa': '5f2 6s2 6p6 6d1 7s2',
        'U': '5f3 6s2 6p6 6d1 7s2',
        'Np': '5f4 6s2 6p6 6d1 7s2',
        'Cm': '5f7 6s2 6p6 6d1 7s2'
    }

    result = []

    while atomic > 0:
        orbital = filling.pop(0)
        if orbital[-1] == 's':
            if atomic > 1:
                result.append(orbital + '2')
                atomic -= 2
            else:
                result.append(orbital + '1')
                atomic -= 1
        elif orbital[-1] == 'p':
            if atomic > 5:
                result.append(orbital + '6')
                atomic -= 6
            else:
                result.append(orbital + str(atomic))
                atomic -= atomic
        elif orbital[-1] == 'd':
            if atomic > 9:
                result.append(orbital + '10')
                atomic -= 10
            else:
                result.append(orbital + str(atomic))
                atomic -= atomic
        elif orbital[-1] == 'f':
            if atomic > 13:
                result.append(orbital + '14')
                atomic -= 14
            else:
                result.append(orbital + str(atomic))
                atomic -= atomic

    result.sort(key=orbital_sort)
    result = f"{element} -> {' '.join(result)}"

    print(element)
    if element in replace_d:
        i = result.index(replace_d[element][:2])
        print((i, result[:i], replace_d[element]))
        result = result[:i] + replace_d[element]

    return result
