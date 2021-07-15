def find_gatecrashers(people, invitations):
    inv_set = set()
    for i in invitations:
        inv_set.add(i[0])
        inv_set.update(i[1])
    res = sorted(list(set(people)-inv_set))
    return res
