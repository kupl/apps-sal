def fight_resolve(defender, attacker):

    if defender.isupper() == attacker.isupper():
        return -1

    battle = dict(zip('ksapKSAP', 'APSKapsk'))
    return defender if battle[defender] == attacker else attacker
