ELEMENTS = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
order=['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s',
       '4f','5d','6p','7s','5f','6d','7p']
hold={'s':2,'p':6,'d':10,'f':14}
special={
    'Cr':['3d5', '4s1'], 'Cu':['3d10', '4s1'], 'Nb':['4d4', '5s1'],
    'Mo':['4d5', '5s1'], 'Ru':['4d7', '5s1'], 'Rh':['4d8', '5s1'],
    'Pd':['4d10', '5s0'], 'Ag':['4d10', '5s1'], 'La':['4f0', '5d1'],
    'Ce':['4f1', '5d1'], 'Gd':['4f7', '5d1', '6s2'], 'Pt':['4f14', '5d9', '6s1'],
    'Au':['4f14', '5d10', '6s1'], 'Ac':['5f0', '6d1', '7s2'],
    'Th':['5f0', '6d2', '7s2'], 'Pa':['5f2', '6d1', '7s2'],
    'U':['5f3', '6d1', '7s2'], 'Np':['5f4', '6d1', '7s2'],
    'Cm':['5f7', '6d1', '7s2']
}
def get_electron_configuration(element):
    e=ELEMENTS.index(element)+1
    r=[]
    for o in order:
        r.append(o+str(min(e,hold[o[1]])))
        e-=hold[o[1]]
        if e<=0:
            break
    if element in special:
        for o2 in special[element]:
            flag=False
            for i in range(len(r)):
                if r[i][:2]==o2[:2]:
                    r[i]=o2
                    flag=True
                    break
            if not flag:
                r.append(o2)
    return '{} -> {}'.format(element,' '.join(sorted(r,key=lambda x:(x[0],'spdf'.index(x[1])))))    
