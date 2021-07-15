from fractions import gcd
def final_attack_value(x,monster_list):
    for i in monster_list:
        x += gcd(i,x) if i > x else i
    return x
