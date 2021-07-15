ELEMENTS = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og']
# Tuple of shell loading.
# (<orbit>, <final count>, <code>)
# Codes are:
#    -2 - Remove one electron at a time and ultimately remove the shell so we don't get something like 5d0 for this one.
#    -1 - Remove electrons in this shell one at a time.  Don't remove the shell.
#     0 - Add this shell with zero electrons so that it does show up as something like 5d0 in the sequence.
#     1 - Add 1 at a time
#     2 - Add but the first one is a double skip because of electrons dropped before.

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
    ("4s", 1, -1), # Cu
    ("3d", 10, 1), # Cu
    ("4s", 2, 1), # Zn
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
    ("6s", 2, 2), # Ba
    ("4f", 0, 0), # La
    ("5d", 1, 1), # La
    ("4f", 1, 1), # Ce
    ("5d", 0, -2), #Pr
    ("4f", 7, 2), # Eu
    ("5d", 1, 1),
    ("5d", 0, -2),
    ("4f", 14, 1), # Yb
    ("5d", 7, 1), # IR
    ("6s", 1, -1), # Pt
    ("5d", 10, 1), # Au
    ("6s", 2, 1), # Hg
    ("6p", 6, 1), # Rn
    ("7s", 2, 1), # Ra
    ("5f", 0, 0), # Ac
    ("6d", 2, 1), # Th
    ("6d", 1, -1), # Pa
    ("5f", 4, 2), # Np
    ("6d", 0, -2), #Pu
    ("5f", 7, 2), # Am
    ("6d", 1, 1), # Cm
    ("6d", 0, -2), # Bk
    ("5f", 14, 2), # No
    ("6d", 1, 1), # Lr
#  These exceptions should exist per https://ptable.com/ but they don't in the tests.
#    ("7p", 1, 1), # Lr
#    ("7p", 0, -2), # Rf
#    ("6d", 7, 2), # Mt
#    ("7s", 1, -1), # Ds
    ("6d", 9, 2), # Ds
    ("7s", 2, 1), # Rg
    ("6d", 10, 1), # Cn
    ("7p", 6, 1)
    )
    
# Order of shells.    
shell_seq = ["1s", "2s", "2p", "3s", "3p", "3d", "4s", "4p", "4d", "4f", "5s", "5p", "5d", "5f", "6s", "6p", "6d", "7s", "7p"]
    
def get_electron_configuration(element):
    # Create our electron shell dictionary
    e = {}
    # Get the atomic number
    a = ELEMENTS.index(element)+1
    # Keep track of the total number electrons.  This is easier/faster than summing up the numbers in the dict.
    t = 0
    # Loop through the shells
    for o, cnt, code in shells:
        # If we reached the atomic number, we stop.
        if t == a:
            break
        else:
            # If orbit isn't in the dict, add it.
            # Note:  Even if code=0 this portion will add the orbit so it will show up in "o in e" below when building the o_list.
            if o not in e: e[o] = 0
            # If the code is -2, count down and delete the orbit.
            if code == -2:
                while e[o] > cnt:
                    e[o] -= 1
                    t -= 1
                del(e[o])
            # If the code is -1, count down.
            elif code == -1:
                while e[o] > cnt:
                    e[o] -= 1
                    t -= 1
            # IF the code is positve, count up.  We just use the 2 for ease in building the table above.
            # Nothing special is required for code=2 vs code=1
            elif code > 0:
                while t != a and e[o] < cnt:
                    e[o] += 1
                    t += 1
    
    # Combine the orbits and counts.  Use the shell_seq to get the order correct and don't include shells that aren't in e.
    o_list = [f"{o}{e[o]}" for o in shell_seq if o in e]
    # Join the list and output.
    return f"{element} -> {' '.join(o_list)}"

