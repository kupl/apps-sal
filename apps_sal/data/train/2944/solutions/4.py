ELEMENTS = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']


def get_electron_configuration(element):
    elems = {
        "Cr": ("3d5 4s1"),
        "Cu": ("3d10 4s1"),
        "Nb": ("4d4 5s1"),
        "Mo": ("4d5 5s1"),
        'Ru': ("4d7 5s1"),
        'Rh': ("4d8 5s1"),
        'Pd': ("4d10 5s0"),
        'Ag': ("4d10 5s1"),
        'La': ("4f0 5d1"),
        'Ce': ("4f1 5d1"),
        'Gd': ("4f7 5d1 6s2"),
        'Pt': ("4f14 5d9 6s1"),
        'Au': ("4f14 5d10 6s1"),
        'Ac': ("5f0 6d1 7s2"),
        'Th': ("5f0 6d2 7s2"),
        'Pa': ("5f2 6d1 7s2"),
        'U': ("5f3 6d1 7s2"),
        'Np': ("5f4 6d1 7s2"),
        'Cm': ("5f7 6d1 7s2"),
    }
    elem_config = elems.get(element)
    list = ['Cr', 'Cu', 'Nb', 'Mo', 'Ru', 'Rh', 'Pd', 'Ag',
            'La', 'Ce', 'Gd', 'Pt', 'Au', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Cm']
    s = []
    c = 0
    a = 0
    for x in range(len(ELEMENTS)):
        if element == ELEMENTS[x]:
            v = x + 1
    if element in list:
        s = elem_config.split(' ')
        for b in s:
            v -= int(b[2:])
    while v > 0:
        c += 1
        if v >= 2:
            s.append(str(c) + "s2")
            v -= 2
        elif 0 < v < 2:
            s.append(str(c) + "s" + str(v))
            v -= v
        if v >= 6 and c > 1:
            s.append(str(c) + "p6")
            v -= 6
        elif 0 < v < 6 and c > 1:
            s.append(str(c) + "p" + str(v))
            v -= v
        if v >= 12 and c > 2:
            s.append(str(c) + "d10")
            v -= 10
        elif 2 < v <= 12 and c > 2:
            s.append(str(c) + "d" + str(v - 2))
            v -= v - 2
        if v >= 24 and c > 3:
            s.append(str(c) + "f14")
            v -= 14
        elif 10 < v < 24 and c > 3:
            s.append(str(c) + "f" + str(v - 10))
            v -= v - 10
    s.sort(key=lambda p: p[0] + {"s": "0", "p": "1", "d": "2", "f": "3"}[p[1]])
    s = " ".join(s)
    return element + " -> " + s
