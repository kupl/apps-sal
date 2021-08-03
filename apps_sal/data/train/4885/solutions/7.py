def find_gatecrashers(people, invitations):
    legit_people = []
    combo_breakers = []
    for ell in invitations:
        for ell2 in ell:
            if isinstance(ell2, int):
                legit_people.append(ell2)
            elif isinstance(ell2, list):
                for ell3 in ell2:
                    legit_people.append(ell3)

    legit_people = set(legit_people)
    for ell4 in people:
        if ell4 not in legit_people:
            combo_breakers.append(ell4)

    return sorted(list(combo_breakers))
