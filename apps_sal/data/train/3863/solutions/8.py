from math import gcd
def final_attack_value(x,monster_list):
    for monster in monster_list:
        if monster>x:x+=gcd(x,monster)
        else:x+=monster
    return x
