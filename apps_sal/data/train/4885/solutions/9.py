def find_gatecrashers(people, invitations):
    known = set()
    for (inviting, invited) in invitations:
        known.add(inviting)
        known |= set(invited)
    return [p for p in people if p not in known]
