ELEMENTS = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
EXCEPTIONS = {
    'Cr': ['Ar', '4s1 3d5'],
    'Cu': ['Ar', '4s1 3d10'],
    'Nb': ['Kr', '5s1 4d4'],
    'Mo': ['Kr', '5s1 4d5'],
    'Ru': ['Kr', '5s1 4d7'],
    'Rh': ['Kr', '5s1 4d8'],
    'Pd': ['Kr', '5s0 4d10'],
    'Ag': ['Kr', '5s1 4d10'],
    'La': ['Xe', '6s2 4f0 5d1'],
    'Ce': ['Xe', '6s2 4f1 5d1'],
    'Gd': ['Xe', '6s2 4f7 5d1'],
    'Pt': ['Xe', '6s1 4f14 5d9'],
    'Au': ['Xe', '6s1 4f14 5d10'],
    'Ac': ['Rn', '7s2 5f0 6d1'],
    'Th': ['Rn', '7s2 5f0 6d2'],
    'Pa': ['Rn', '7s2 5f2 6d1'],
    'U' : ['Rn', '7s2 5f3 6d1'],
    'Np': ['Rn', '7s2 5f4 6d1'],
    'Cm': ['Rn', '7s2 5f7 6d1'],
}
ORBITALS = "spdfg"
ELT_TO_Z = {elt:i for i,elt in enumerate(ELEMENTS,1)}
for arr in list(EXCEPTIONS.values()):
    arr[1] = [ (int(s[0]), ORBITALS.find(s[1]), s[2:]) for s in arr[1].split(' ') ]


def get_electron_configuration(element):
    elt,repl = EXCEPTIONS.get(element, (element,[]) )
    z,nl,config = ELT_TO_Z[elt], 0, {}                  # n: principal quantum number / l: secondary qunatum number (minus 1) / nl: n+l
    while z:
        nl += 1
        for l in range(nl-1>>1, -1, -1):
            nE = min(z, 2+l*4)
            config[ (nl-l,l) ] = nE
            z -= nE
            if not z: break
    
    for a,b,n in repl: config[(a,b)] = n
    
    s = " ".join( f'{ k[0] }{ ORBITALS[k[1]] }{ n }' for k,n in sorted(config.items()))
    return f'{ element } -> { s }'

