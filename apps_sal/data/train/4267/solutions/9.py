classes = {
    "warrior":     {"start": 4,  "stats": [11, 8, 12, 13, 13, 11, 9, 9]},
    "knight":      {"start": 5,  "stats": [14, 10, 10, 11, 11, 10, 9, 11]},
    "wanderer":    {"start": 3,  "stats": [10, 11, 10, 10, 14, 12, 11, 8]},
    "thief":       {"start": 5,  "stats": [9, 11, 9, 9, 15, 10, 12, 11]},
    "bandit":      {"start": 4,  "stats": [12, 8, 14, 14, 9, 11, 8, 10]},
    "hunter":      {"start": 4,  "stats": [11, 9, 11, 12, 14, 11, 9, 9]},
    "sorcerer":    {"start": 3,  "stats": [8, 15, 8, 9, 11, 8, 15, 8]},
    "pyromancer":  {"start": 1,  "stats": [10, 12, 11, 12, 9, 12, 10, 8]},
    "cleric":      {"start": 2,  "stats": [11, 11, 9, 12, 8, 11, 8, 14]},
    "deprived":    {"start": 6,  "stats": [11, 11, 11, 11, 11, 11, 11, 11]},
}

requirements = [0, 673, 690, 707, 724, 741, 758, 775, 793, 811, 829]

def souls(character, build):
    diff = sum(b - s for b, s in zip(build, classes[character]["stats"]))
    level = classes[character]["start"] + diff
    required = sum(x for x in requirements[classes[character]["start"]:level])
    required += sum(round(0.02*x**3+3.06*x**2+105.6*x-895) for x in range(12, level+1))
    return "Starting as a {}, level {} will require {} souls.".format(character, level, required)
