def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def final_attack_value(x, monster_list):
    for m in monster_list:
        x = x + m if m <= x else x + gcd(x, m)
    return x
