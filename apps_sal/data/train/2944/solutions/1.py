ELEMENTS = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
import re

exc = '''Cr -> ...3d5 4s1
Cu -> ...3d10 4s1
Nb -> ...4d4 5s1
Mo -> ...4d5 5s1
Ru -> ...4d7 5s1
Rh -> ...4d8 5s1
Pd -> ...4d10 5s0
Ag -> ...4d10 5s1
La -> ...4f0 5d1
Ce -> ...4f1 5d1
Gd -> ...4f7 5d1 6s2
Pt -> ...4f14 5d9 6s1
Au -> ...4f14 5d10 6s1
Ac -> ...5f0 6d1 7s2
Th -> ...5f0 6d2 7s2
Pa -> ...5f2 6d1 7s2
U  -> ...5f3 6d1 7s2
Np -> ...5f4 6d1 7s2
Cm -> ...5f7 6d1 7s2'''
exceptions = {i.split()[0]: {j[:2]: j[2:] for j in i.split('...')[1].split()} for i in exc.split('\n')}

def get_electron_configuration(element):
    names = re.findall(r'..', '1s2s2p3s3p4s3d4p5s4d5p6s4f5d6p7s5f6d7p8s')
    values = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6, 2]
    N = ELEMENTS.index(element) + 1
    res = {}
    while N > 0:
        v = min(values.pop(0), N)
        res[names.pop(0)] = str(v)
        N -= v
    if element in exceptions:
        res.update(exceptions[element])
    res = [i+j for i,j in zip(res.keys(), res.values())]
    res.sort(key = lambda x: (x[0], ['s', 'p', 'd', 'f'].index(x[1])))
    return '{} -> {}'.format(element, ' '.join(res))
