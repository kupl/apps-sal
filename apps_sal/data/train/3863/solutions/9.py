def gcd(a, b):
    while a != b:

        if a > b:
            a = a - b
        if b > a:
            b = b - a
    return a


def final_attack_value(x, monster_list):
    for i in monster_list:
        if x > i:
            x += i
        else:
            x += gcd(x, i)
    return x
