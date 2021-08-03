ELEMENTS = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']


def get_electron_configuration(a):
    d = {"s": 2, "p": 6, "d": 10, "f": 14}
    o = [[x, d[x[1]]] for x in ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p", "6s", "4f", "5d", "6p", "7s", "5f", "6d", "7p"]][::-1]
    exceptions = {"Cr": [2, "4s1 3d5"], "Cu": [2, "4s1 3d10"], "Nb": [2, "5s1 4d4"], "Mo": [2, "5s1 4d5"], "Ru": [2, "5s1 4d7"], "Rh": [2, "5s1 4d8"], "Pd": [2, "5s0 4d10"], "Ag": [2, "5s1 4d10"], "La": [1, "4f0 5d1"], "Ce": [1, "4f1 5d1"], "Gd": [1, "4f7 5d1"], "Pt": [3, "6s1 4f14 5d9"], "Au": [3, "6s1 4f14 5d10"], "Ac": [1, "5f0 6d1"], "Th": [1, "5f0 6d2"], "Pa": [1, "5f2 6d1"], "U": [1, "5f3 6d1"], "Np": [1, "5f4 6d1"], "Cm": [1, "5f7 6d1"]}
    r, n = [], ELEMENTS.index(a) + 1
    while n > 0:
        s, m = o.pop()
        x = min(n, m)
        n -= x
        r.append("{}{}".format(s, x))
    if a in exceptions:
        m, s = exceptions[a]
        r = r[:-m] + s.split()
    return "{} -> {}".format(a, " ".join(sorted(r, key=lambda x: (x[0], d[x[1]]))))
