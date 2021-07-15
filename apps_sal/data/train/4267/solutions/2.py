CLASSES = {"warrior": {"stats": [11, 8, 12, 13, 13, 11, 9, 9], "lvl": 4},
           "knight": {"stats": [14, 10, 10, 11, 11, 10, 9, 11], "lvl": 5},
           "wanderer": {"stats": [10, 11, 10, 10, 14, 12, 11, 8], "lvl": 3},
           "thief": {"stats": [9, 11, 9, 9, 15, 10, 12, 11], "lvl": 5},
           "bandit": {"stats": [12, 8, 14, 14, 9, 11, 8, 10], "lvl": 4},
           "hunter": {"stats": [11, 9, 11, 12, 14, 11, 9, 9], "lvl": 4},
           "sorcerer": {"stats": [8, 15, 8, 9, 11, 8, 15, 8], "lvl": 3},
           "pyromancer": {"stats": [10, 12, 11, 12, 9, 12, 10, 8], "lvl": 1},
           "cleric": {"stats": [11, 11, 9, 12, 8, 11, 8, 14], "lvl": 2},
           "deprived": {"stats": [11, 11, 11, 11, 11, 11, 11, 11], "lvl": 6}}

def souls(character, build):
    required_lvl = sum(build) - sum(CLASSES[character]["stats"]) + CLASSES[character]["lvl"]
    souls_needed = sum([calc_exp(lvl) for lvl in range(CLASSES[character]["lvl"] + 1, required_lvl + 1)])
    return f"Starting as a {character}, level {required_lvl} will require {souls_needed} souls."

def calc_exp(lvl):
    return 673 + 17 * (lvl - 2) if lvl <= 8 else 775 + 18 * (lvl - 8) if lvl <= 11 else round(pow(lvl, 3) * 0.02 + pow(lvl, 2) * 3.06 + 105.6 * lvl - 895)
