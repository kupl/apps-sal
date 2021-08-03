def find_gatecrashers(people, invitations):
    ok = set()
    for i in invitations:
        a, b = i
        ok.add(a)
        for ii in b:
            ok.add(ii)

    return sorted(list(set(people) - ok))
