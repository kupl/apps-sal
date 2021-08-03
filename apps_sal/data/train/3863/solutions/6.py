def final_attack_value(x, monster_list):
    for i in monster_list:
        if x >= i:
            x += i
        else:
            a = x
            b = i
            while b:
                a, b = b, a % b
            x += a
    return x
