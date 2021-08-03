from math import gcd


def final_attack_value(x, monster_list):
    for m in monster_list:
        if m <= x:
            x += m
        else:
            x += gcd(x, m)
    return x
