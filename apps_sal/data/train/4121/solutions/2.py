def fight_resolve(defender, attacker):
    res = attacker
    if defender.islower() and attacker.islower() or defender.isupper() and attacker.isupper():
        return -1
    elif attacker.lower() == 'a':
        if defender.lower() == 'k':
            res = defender
    elif attacker.lower() == 'p':
        if defender.lower() == 's':
            res = defender
    elif attacker.lower() == 's':
        if defender.lower() == 'a':
            res = defender
    elif attacker.lower() == 'k':
        if defender.lower() == 'p':
            res = defender
    return res

