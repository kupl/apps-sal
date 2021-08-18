ELEMENTS = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']


def get_electron_configuration(element):
    '''
    Return the electron configuration of the supplied element.
    '''

    exceptions = \
        {"Cr": ["3d5", "4s1"],
         "Cu": ["3d10", "4s1"],
         "Nb": ["4d4", "5s1"],
         "Mo": ["4d5", "5s1"],
         "Ru": ["4d7", "5s1"],
         "Rh": ["4d8", "5s1"],
         "Pd": ["4d10", "5s0"],
         "Ag": ["4d10", "5s1"],
         "La": ["4f0", "5d1"],
         "Ce": ["4f1", "5d1"],
         "Gd": ["4f7", "5d1", "6s2"],
         "Pt": ["4f14", "5d9", "6s1"],
         "Au": ["4f14", "5d10", "6s1"],
         "Ac": ["5f0", "6d1", "7s2"],
         "Th": ["5f0", "6d2", "7s2"],
         "Pa": ["5f2", "6d1", "7s2"],
         "U": ["5f3", "6d1", "7s2"],
         "Np": ["5f4", "6d1", "7s2"],
         "Cm": ["5f7", "6d1", "7s2"]}

    orbitals = ["1s2", "2s2", "2p6", "3s2", "3p6", "4s2", "3d10", "4p6", "5s2",
                "4d10", "5p6", "6s2", "4f14", "5d10", "6p6", "7s2", "5f14",
                "6d10", "7p6", "8s2"]

    atomicNumber = ELEMENTS.index(element) + 1
    numElectrons = atomicNumber
    orbitalIndex = 0
    config = []

    while numElectrons > 0:
        if numElectrons - int(orbitals[orbitalIndex][2:]) > 0:
            config.append(orbitals[orbitalIndex])
        else:
            config.append(orbitals[orbitalIndex][:2] + str(numElectrons))

        numElectrons -= int(orbitals[orbitalIndex][2:])
        orbitalIndex += 1

    if element in list(exceptions.keys()):
        end = exceptions[element]
        e = 0
        for orb in end:
            e += int(orb[2:])
        while e > 0:
            e -= int(config.pop()[2:])

        config.extend(end)

    return element + " -> " + " ".join(sorted(config, key=lambda x: x[0]))
