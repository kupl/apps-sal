ELEMENTS = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']


def get_electron_configuration(element):
    atomic_no, n = ELEMENTS.index(element) + 1, 0
    orbitals = {'1s': 0, '2s': 0, '2p': 0, '3s': 0, '3p': 0, '3d': 0, '4s': 0, '4p': 0, '4d': 0, '4f': 0, '5s': 0, '5p': 0, '5d': 0, '5f': 0, '6s': 0, '6p': 0, '6d': 0, '6f': 0, '7s': 0, '7p': 0, '7d': 0, '7f': 0}
    exceptions = {'Cr': 'Cr -> 1s2 2s2 2p6 3s2 3p6 3d5 4s1', 'Cu': 'Cu -> 1s2 2s2 2p6 3s2 3p6 3d10 4s1', 'Nb': 'Nb -> 1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d4 5s1', 'Mo': 'Mo -> 1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d5 5s1', 'Ru': 'Ru -> 1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d7 5s1', 'Rh': 'Rh -> 1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d8 5s1', 'Pd': 'Pd -> 1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s0', 'Ag': 'Ag -> 1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s1', 'La': 'La -> 1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f0 5s2 5p6 5d1 6s2', 'Ce': 'Ce -> 1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f1 5s2 5p6 5d1 6s2', 'Gd': 'Gd -> 1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f7 5s2 5p6 5d1 6s2', 'Pt': 'Pt -> 1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d9 6s1', 'Au': 'Au -> 1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s1', 'Ac': 'Ac -> 1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f0 6s2 6p6 6d1 7s2', 'Th': 'Th -> 1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f0 6s2 6p6 6d2 7s2', 'Pa': 'Pa -> 1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f2 6s2 6p6 6d1 7s2', 'U': 'U -> 1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f3 6s2 6p6 6d1 7s2', 'Np': 'Np -> 1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f4 6s2 6p6 6d1 7s2', 'Cm': 'Cm -> 1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f7 6s2 6p6 6d1 7s2'}
    if element in exceptions:
        return exceptions[element]
    while n < atomic_no:
        if n < 2:
            orbitals['1s'] += 1
        elif n < 4:
            orbitals['2s'] += 1
        elif n < 10:
            orbitals['2p'] += 1
        elif n < 12:
            orbitals['3s'] += 1
        elif n < 18:
            orbitals['3p'] += 1
        elif n < 20:
            orbitals['4s'] += 1
        elif n < 30:
            orbitals['3d'] += 1
        elif n < 36:
            orbitals['4p'] += 1
        elif n < 38:
            orbitals['5s'] += 1
        elif n < 48:
            orbitals['4d'] += 1
        elif n < 54:
            orbitals['5p'] += 1
        elif n < 56:
            orbitals['6s'] += 1
        elif n < 70:
            orbitals['4f'] += 1
        elif n < 80:
            orbitals['5d'] += 1
        elif n < 86:
            orbitals['6p'] += 1
        elif n < 88:
            orbitals['7s'] += 1
        elif n < 102:
            orbitals['5f'] += 1
        elif n < 112:
            orbitals['6d'] += 1
        elif n < 118:
            orbitals['7p'] += 1
        n += 1
    st = ''
    orbs = ['1s', '2s', '2p', '3s', '3p', '3d', '4s', '4p', '4d', '4f', '5s', '5p', '5d', '5f', '6s', '6p', '6d', '6f', '7s', '7p', '7d', '7f']
    for x in orbs:
        if orbitals[x] != 0:
            st += x + str(orbitals[x]) + ' '
    return element + ' -> ' + st.rstrip()
