def calculate_damage(your_type, opponent_type, attack, defense):
    damage = 50 * (attack / defense)
    if your_type == opponent_type:
        return int(damage * 0.5)
        
    pairs = (('water', 'fire'), ('fire', 'grass'), ('grass', 'water'), ('electric', 'water'))
    e = 1
    for p in pairs:
        if your_type in p and opponent_type in p:
            if p.index(your_type) == 0:
                e = 2
            else:
                e = 0.5
    return int(damage * e)
