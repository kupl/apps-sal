def find_gatecrashers(people, invitations):
    crashersSet = {elt for i, li in invitations for elt in [i] + li}
    return [p for p in people if p not in crashersSet]
