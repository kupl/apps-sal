import math


def calculate_damage(your_type, opponent_type, attack, defense):
    powerMap = {
        ('fire', 'grass'): 2,
        ('water', 'fire'): 2,
        ('fire', 'electric'): 1,
        ('grass', 'water'): 2,
        ('electric', 'water'): 2,
        ('grass', 'electric'): 1

    }
    print((your_type, opponent_type, attack, defense))
    effectiveness = 0
    if your_type == opponent_type or ((opponent_type, your_type) in powerMap and powerMap[(opponent_type, your_type)] == 2):
        effectiveness = 0.5
    elif (your_type, opponent_type) in powerMap:
        effectiveness = powerMap[(your_type, opponent_type)]
    elif (opponent_type, your_type) in powerMap and powerMap[(opponent_type, your_type)] == 1:
        effectiveness = 1

    return math.ceil(attack / defense * 50 * effectiveness)
