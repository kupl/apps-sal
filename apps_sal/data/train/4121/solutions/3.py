def fight_resolve(defender, attacker):
    if attacker.isupper() and defender.isupper() or (attacker.islower() and defender.islower()):
        return -1
    att = {'A': 1, 'P': 2, 'S': 3, 'K': 4}
    dff = {'K': 1, 'S': 2, 'A': 3, 'P': 4}
    if att[attacker.upper()] == dff[defender.upper()]:
        return defender
    else:
        return attacker
