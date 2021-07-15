from functools import reduce
from fractions import gcd

def final_attack_value(x, monster_list):
    return reduce(lambda a, b: a + (b if b <= a else gcd(a, b)), monster_list, x)
