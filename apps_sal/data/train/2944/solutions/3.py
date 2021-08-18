ELEMENTS = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']

shells = (
    ("1s", 2, 1),
    ("2s", 2, 1),
    ("2p", 6, 1),
    ("3s", 2, 1),
    ("3p", 6, 1),
    ("4s", 2, 1),
    ("3d", 3, 1),
    ("4s", 1, -1),
    ("3d", 5, 2),
    ("4s", 2, 1),
    ("3d", 8, 1),
    ("4s", 1, -1),
    ("3d", 10, 1),
    ("4s", 2, 1),
    ("4p", 6, 1),
    ("5s", 2, 1),
    ("4d", 2, 1),
    ("5s", 1, -1),
    ("4d", 5, 2),
    ("5s", 2, 1),
    ("5s", 1, -1),
    ("4d", 8, 2),
    ("5s", 0, -1),
    ("4d", 10, 2),
    ("5s", 2, 1),
    ("5p", 6, 1),
    ("6s", 2, 2),
    ("4f", 0, 0),
    ("5d", 1, 1),
    ("4f", 1, 1),
    ("5d", 0, -2),
    ("4f", 7, 2),
    ("5d", 1, 1),
    ("5d", 0, -2),
    ("4f", 14, 1),
    ("5d", 7, 1),
    ("6s", 1, -1),
    ("5d", 10, 1),
    ("6s", 2, 1),
    ("6p", 6, 1),
    ("7s", 2, 1),
    ("5f", 0, 0),
    ("6d", 2, 1),
    ("6d", 1, -1),
    ("5f", 4, 2),
    ("6d", 0, -2),
    ("5f", 7, 2),
    ("6d", 1, 1),
    ("6d", 0, -2),
    ("5f", 14, 2),
    ("6d", 1, 1),
    ("6d", 9, 2),
    ("7s", 2, 1),
    ("6d", 10, 1),
    ("7p", 6, 1)
)

shell_seq = ["1s", "2s", "2p", "3s", "3p", "3d", "4s", "4p", "4d", "4f", "5s", "5p", "5d", "5f", "6s", "6p", "6d", "7s", "7p"]


def get_electron_configuration(element):
    e = {}
    a = ELEMENTS.index(element) + 1
    t = 0
    for o, cnt, code in shells:
        if t == a:
            break
        else:
            if o not in e:
                e[o] = 0
            if code == -2:
                while e[o] > cnt:
                    e[o] -= 1
                    t -= 1
                del(e[o])
            elif code == -1:
                while e[o] > cnt:
                    e[o] -= 1
                    t -= 1
            elif code > 0:
                while t != a and e[o] < cnt:
                    e[o] += 1
                    t += 1

    o_list = [f"{o}{e[o]}" for o in shell_seq if o in e]
    return f"{element} -> {' '.join(o_list)}"
