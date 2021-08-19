def fight_resolve(defender, attacker):
    fight = (defender + attacker).lower()
    d_low = defender == defender.lower()
    a_low = attacker == attacker.lower()
    if d_low and a_low or (not d_low and (not a_low)):
        return -1
    if 'a' in defender.lower() and 's' in attacker.lower():
        winner = defender
    elif 's' in defender.lower() and 'p' in attacker.lower():
        winner = defender
    elif 'p' in defender.lower() and 'k' in attacker.lower():
        winner = defender
    elif 'k' in defender.lower() and 'a' in attacker.lower():
        winner = defender
    else:
        winner = attacker
    return winner
