from math import gcd

def final_attack_value(attack, monsters):
    for monster in monsters:
        attack += gcd(attack, monster) if attack < monster else monster
    return attack
