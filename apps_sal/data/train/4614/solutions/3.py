SCORES = {
    'chickenwings': 5,
    'hamburgers': 3,
    'hambrgers': 3,
    'hotdogs': 2,
}

def scoreboard(who_ate_what):
    return sorted([
        {
            'name': d['name'],
            'score': sum(SCORES[food] * count for food, count in d.items() if food != 'name')
        }
        for d in who_ate_what
    ], key=lambda d: (-d['score'], d['name']))
