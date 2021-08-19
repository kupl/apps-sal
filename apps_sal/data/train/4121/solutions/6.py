def fight_resolve(defender, attacker):
    if defender.islower() == attacker.islower():
        return -1
    return defender if f'{defender}{attacker}'.lower() in 'aspka' else attacker
